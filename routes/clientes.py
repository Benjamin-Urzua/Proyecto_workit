from flask import Blueprint, render_template

clientes = Blueprint('clientes', __name__)

@clientes.route("/clientes/leer")
def leer():
    return render_template('leer.html')

@clientes.route("/clientes/crear")
def crear():
    return render_template('/clientes/crear.html')

@clientes.route("/clientes/actualizar")
def actualizar():
    return render_template('actualizar.html')

@clientes.route("/clientes/eliminar")
def eliminar():
    return render_template('eliminar.html')