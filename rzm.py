from flask import Flask,render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_session import Session
from flask_mysqldb import MySQL 
import os
import base64
from flask import Flask, render_template, request, flash, redirect, url_for


UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rzm'

mysql = MySQL(app)
 
@app.route('/')
def accedi():

    return render_template('rzm/accedi.html')





@app.route("/logout")
def logout():
    session["email"] = None
    return redirect("/")






#registrarsi
@app.route('/data/', methods=['POST'])
def data():
    form_data = request.form
    emailform=request.form['email']
    nomeform=request.form['nome']
    cognomeform=request.form['cognome']
    pwdform=request.form['pwd']

    cursore=mysql.connection.cursor()
    cursore.execute("INSERT INTO utenti VALUES ('"+emailform+"' , '"+nomeform+"' , '"+cognomeform+"' , '"+pwdform+"')")
    mysql.connection.commit()
    cursore.close()
    return render_template('rzm/avviso.html')




#accedere
@app.route('/accesso', methods=['POST'])
def accesso():
    email = request.form['email']
    password = request.form['password']
    session["email"] = email

    cursor=mysql.connection.cursor()
    query = 'SELECT nome FROM utenti WHERE email = %s AND password = %s'
    cursor.execute(query, (email, password))
    session["nome"] = cursor.fetchone()[0 ]


    query = 'SELECT * FROM utenti WHERE email = %s AND password = %s'
    cursor.execute(query, (email, password))
    utente = cursor.fetchone()

    if utente:

        return redirect('/home')
    else:

        return render_template('rzm/accedi.html', error='Credenziali non valide.')





@app.route('/home')
def home():
    if not session.get("email"):
        # if not there in the session then redirect to the login page
        return redirect("/")
    current_session = session.get("nome")
    return render_template('rzm/home.html', current_session=current_session)




@app.route('/maglie')
def maglie():
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM merce WHERE categoria = 'maglie'")
    posts = [dict(id=row[0], nome=row[1], descrizione=row[2], taglia=row[4], prezzo=row[5], immagine=row[6])for row in cursore.fetchall()]
    if len(posts) == 0:
        return render_template("oops... non abbiamo prodotti disponibili :(")
    else:
        return render_template("rzm/scarpe.html", p=posts)





# App route per Scarpe
@app.route('/scarpe')
def scarpe():
    if not session.get("email"):
        # if not there in the session then redirect to the login page
        return redirect("/")
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM merce WHERE categoria = 'scarpe'")
    posts = [dict(id=row[0], nome=row[1], descrizione=row[2], taglia=row[4], prezzo=row[5], immagine=row[6])for row in cursore.fetchall()]
    if len(posts) == 0:
        return render_template("Azienda/visual.html", a="non ha funzionato")
    else:
        return render_template("rzm/scarpe.html", p=posts)





@app.route('/felpe')
def felpe():
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM merce WHERE categoria = 'felpe'")
    posts = [dict(id=row[0], nome=row[1], descrizione=row[2], taglia=row[4], prezzo=row[5], immagine=row[6])for row in cursore.fetchall()]
    if len(posts) == 0:
        return render_template("Azienda/visual.html", a="non ha funzionato")
    else:
        return render_template("rzm/scarpe.html", p=posts)




@app.route('/vendi')
def vendi():
    if not session.get("email"):
        # if not there in the session then redirect to the login page
        return redirect("/")
    return render_template('rzm/vendi.html')






#venduto
@app.route('/venduto', methods=['POST'])
def venduto():
    nome = request.form['nome']
    categoria = request.form['categoria']
    descrizione = request.form['descrizione']
    taglia = request.form['taglia']
    prezzo = request.form['prezzo']
    immagine = request.files['immagine']

    filename = secure_filename(immagine.filename)
    immagine.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    

    cursore=mysql.connection.cursor()
    cursore.execute("INSERT INTO merce (nome, descrizione, categoria, taglia, prezzo, immagine) VALUES ('" + nome + "', '" + descrizione + "', '" + categoria + "', '" + taglia + "', '" + prezzo + "', '" + filename + "')")
    mysql.connection.commit()
    cursore.close()
    flash('Il prodotto è stato messo in vendita con successo!!!', 'success')
    return redirect(url_for('vendi'))
    





@app.route('/dettaglio', methods=['GET'])
def dettaglio():
    id = request.args.get('variabile')
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM merce WHERE ID = '" + id + "'")
    posts = [dict(id=row[0], nome=row[1], descrizione=row[2], taglia=row[4], prezzo=row[5], immagine=row[6])for row in cursore.fetchall()]
    return render_template("rzm/prodottoDettaglio.html", p=posts)





if __name__=="__main__":
    app.run(debug=True, port=5000)


  

