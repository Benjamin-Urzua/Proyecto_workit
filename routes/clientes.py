from flask import Blueprint, render_template, request
from models.cliente import RetornarHistorial
from controllers.register import SelectPreguntas
clientes = Blueprint('clientes', __name__)

@clientes.route("/clientes/leer")
def leer():
    return render_template('leer.html')

@clientes.route("/clientes/historial")
def retornar_historial():
    historial = RetornarHistorial("20949993_2")
    return render_template("clientes/historial.html", historial = historial, run = "20949993_2")

@clientes.route("/clientes/registrarse")
def register():
    '''
    if (request.method == "POST"):
        nombres = request.form['txt_nombres']
        apellidos = request.form['txt_apellidos']
        contrasena = request.form['txt_contrasena']
        repetirContrasena = request.form['txt_repetircontrasena']
        calle = request.form['txt_calle']
        nCalle = request.form['txt_nCalle']
        correo = request.form['txt_correo']
        telefono = request.form['txt_telefono']
        preguntaSeguridad = request.form['txt_preguntaSeguridad']
        respuestaSeguridad = request.form['txt_respuestaSeguridad']
    '''
    preguntas = SelectPreguntas()

    return render_template('/clientes/register.html', preguntas = preguntas)

@clientes.route("/clientes/actualizar")
def actualizar():
    return render_template('actualizar.html')

@clientes.route("/clientes/eliminar")
def eliminar():
    return render_template('eliminar.html')