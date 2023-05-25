from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_Password'] = ''
app.config['MYSQL_DB'] = 'azienda'

mysql = MySQL(app)

@app.route('/home')
def home():
    return render_template("Azienda/home.html")

@app.route('/datiBis')
def datiBis():
    return render_template("Azienda/datiBis.html")

@app.route('/data', methods = ['POST'])
def data():
    id = request.form['id']
    nome = request.form['nome']
    quantita = request.form['quantita']
    cursore = mysql.connection.cursor()
    cursore.execute("INSERT INTO magazzino VALUES ('" + id + "', '" + nome + "', '" + quantita + "')")
    mysql.connection.commit()
    cursore.close()
    return render_template("Azienda/datiBis.html")

@app.route('/ricerca', methods = ['POST'])
def ricerca():
    id = request.form['id']
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM magazzino WHERE ID =" + id)
    posts = [dict(id=row[0], nome=row[1], quantita=row[2]) for row in cursore.fetchall()]
    mysql.connection.commit()
    cursore.close()
    if len(posts) == 0:
        return render_template("Azienda/dati.html", a="non ha funzionato")
    else:
        return render_template("Azienda/dati.html", p=posts)

@app.route('/modifica', methods = ['POST'])
def modifica():
    idnome = request.form['id']
    quantita = request.form['quantita']
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM magazzino where ID=" + idnome)
    posts = [dict(ID=row[0], nome=row[1], quantita=row[2])for row in cursore.fetchall()]
    if len(posts) > 0:
        cursore.execute("UPDATE magazzino SET quantita='" +quantita+"' where ID='"+idnome+"'")
        mysql.connection.commit()
        cursore.close()
        return render_template("Azienda/modifica.html", a="completata :)")
    else:
        return render_template("Azienda/modifica.html", a=" non completata :( (id non corretto)")

@app.route('/visualizza', methods = ['POST'])
def visualizza():
    cursore = mysql.connection.cursor()
    cursore.execute("SELECT * FROM magazzino")
    posts = [dict(ID=row[0], nome=row[1], quantita=row[2])for row in cursore.fetchall()]
    if len(posts) == 0:
        return render_template("Azienda/visual.html", a="non ha funzionato")
    else:
        return render_template("Azienda/visual.html", p=posts)


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )