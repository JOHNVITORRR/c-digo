from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template("index.html")

@app.route('/contato')
def segunda_pagina():
    return render_template("contato.html")

@app.route('//final')
def terceira_pagina():
    return render_template("final.html")

