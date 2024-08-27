from mimetypes import init, inited
from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask("name")



@app.route('/')
def index():
    # Conectar ao banco de dados e obter todos os contatos
    with sqlite3.connect('contacts.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM contacts')
        contacts = cur.fetchall()
    return render_template('contacts.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form.get('name')
    email = request.form.get('email')

    # Conectar ao banco de dados e adicionar um novo contato
    with sqlite3.connect('contacts.db') as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO contacts (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
    
    return redirect(url_for('index'))

if "name" == '_main_':

    app.run(debug=True)