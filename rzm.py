from flask import Flask,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_mysqldb import MySQL 
import os
import base64

UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rzm'

mysql = MySQL(app)
 
@app.route('/')
def accedi():
    return render_template('rzm/accedi.html')




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
    return render_template('es7-scuola/Dati2.html')




#accedere
@app.route('/accesso', methods=['POST'])
def accesso():
    email = request.form['email']
    password = request.form['password']

    cursor=mysql.connection.cursor()


    query = 'SELECT * FROM utenti WHERE email = %s AND password = %s'
    cursor.execute(query, (email, password))
    utente = cursor.fetchone()

    if utente:

        return redirect('/home')
    else:

        return render_template('rzm/accedi.html', error='Credenziali non valide.')





@app.route('/home')
def home():
    return render_template('rzm/home.html')




@app.route('/maglie')
def maglie():
    return render_template('rzm/maglie.html')





# App route per Scarpe
@app.route('/scarpe')
def scarpe():
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM merce WHERE categoria = 'scarpe'")
    posts = [dict(id=row[0], nome=row[1], descrizione=row[2], taglia=row[4], prezzo=row[5], immagine=row[6])for row in cursore.fetchall()]
    if len(posts) == 0:
        return render_template("Azienda/visual.html", a="non ha funzionato")
    else:
        return render_template("rzm/scarpe.html", p=posts)
    return render_template('rzm/scarpe.html')





@app.route('/felpe')
def felpe():
    return render_template('rzm/felpe.html')

@app.route('/vendi')
def vendi():
    return render_template('rzm/vendi.html')




#venduto
@app.route('/venduto', methods=['POST'])
def venduto():
    nome = request.form['nome']
    descrizione = request.form['descrizione']
    taglia = request.form['taglia']
    prezzo = request.form['prezzo']
    immagine = request.files['immagine']

    filename = secure_filename(immagine.filename)
    immagine.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    

    cursore=mysql.connection.cursor()
    cursore.execute("INSERT INTO merce (nome, descrizione, categoria, taglia, prezzo, immagine) VALUES ('" + nome + "', '" + descrizione + "', '" + "scarpe" + "', '" + taglia + "', '" + prezzo + "', '" + filename + "')")
    mysql.connection.commit()
    cursore.close()
    return "hai spaccato, <a href='/vendi'>Torna indietro</a>"



if __name__=="__main__":
    app.run(debug=True, port=5000)


  

