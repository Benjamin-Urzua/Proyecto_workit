import json
from flask import Blueprint, make_response, render_template, request, jsonify
from models.cliente import RegistrarProvincia, RetornarHistorial, Register, RegistrarRegion,RegistrarProvincia
from controllers.register import SelectPreguntas
clientes = Blueprint('clientes', __name__)

@clientes.route("/clientes/leer")
def leer():
    return render_template('leer.html')

@clientes.route("/clientes/historial")
def retornar_historial():
    historial = RetornarHistorial("20949993_2")
    return render_template("clientes/historial.html", historial = historial, run = "20949993_2")

@clientes.route("/clientes/registrarse", methods=['POST', 'GET'])
def registrarse():
    preguntas = SelectPreguntas()
    return render_template('/clientes/register.html', preguntas = preguntas)
    
@clientes.route("/clientes/registrarse/guardar", methods=['GET', 'POST'])
def guardar_registro():
    data = request.form.to_dict()
    direccion = data['txt_direccion']
    newDireccion = direccion.split(',')
    newDireccion.pop()
    region = newDireccion[-1]
    RegistrarRegion('XVIII', region, 1)
    RegistrarProvincia()
    print('direccion: {}'.format(region))

    print(data)
    return make_response(data)

'''
@clientes.route("/clientes/resultadosRegistro", methods=['POST'])
def registrarse():
    nombres = request.form['txt_nombres']
    apellidos = request.form['txt_apellidos']
    contrasena = request.form['txt_contrasena']
    repetirContrasena = request.form['txt_repetircontrasena']
    correo = request.form['txt_correo']
    calle = request.form['txt_calle']    
    nCalle = request.form['txt_nCalle']
    fechaNacto = request.form['txt_fechanacto']
    comuna = request.form['txt_comuna']
    telefono = request.form['txt_telefono']
    preguntaSeguridad = request.form['txt_preguntaSeguridad']
    respuestaSeguridad = request.form['txt_respuestaSeguridad']
    
    Register
    
    return "Registrando"
'''
@clientes.route("/clientes/actualizar")
def actualizar():
    return render_template('actualizar.html')

@clientes.route("/clientes/eliminar")
def eliminar():
    return render_template('eliminar.html')