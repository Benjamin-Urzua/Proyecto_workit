import json, requests
from msilib.schema import Billboard
from flask import Blueprint, make_response, render_template, request, jsonify
from models.cliente import  RegistrarDireccion, RegistrarRespuestaSeguridad,  RetornarHistorial, Register
from controllers.register import  SelectPreguntas

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
    calleNum = data['txt_direccion'].split(' ')
    nCalle = calleNum[-1]
    calleNum.pop()
    calle = '+'
    calle = calle.join(calleNum)
    
    
    codigoRegion = data['combo_region']
    regionResponse = requests.get('https://apis.digital.gob.cl/dpa/regiones/{}'.format(codigoRegion), params=[('q', 'requests+language:python')], headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    region = json.loads(regionResponse.text)
    region = region["nombre"].replace(' ', '+')
    
    codigoProvincia = data['combo_provincia'].replace(' ', '+')
    provinciaResponse = requests.get('https://apis.digital.gob.cl/dpa/provincias/{}'.format(codigoProvincia), params=[('q', 'requests+language:python')], headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    provincia = json.loads(provinciaResponse.text)
    provincia = provincia["nombre"].replace(' ', '+')
    
    codigoComuna = data['combo_comuna'].replace(' ', '+')
    comunaResponse = requests.get('https://apis.digital.gob.cl/dpa/comunas/{}'.format(codigoComuna), params=[('q', 'requests+language:python')], headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
    comuna = json.loads(comunaResponse.text)
    comuna = comuna["nombre"].replace(' ', '+')
    
    
    mapsResponse = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}+{}+,+{}+,+{}+,+{}+,+Chile&key=AIzaSyBwOsP73t_qgFi88Wa374i--YZ1ExOLpqQ'.format(nCalle, calle, comuna, provincia, region))
    maps = json.loads(mapsResponse.text)
        
    region = region.replace('+', ' ')
    provincia = provincia.replace('+', ' ')
    comuna = comuna.replace('+', ' ')
    lat = maps["results"][0]["geometry"]["location"]["lat"]
    lng = maps["results"][0]["geometry"]["location"]["lng"]
        
    RegistrarDireccion(region, provincia, comuna,calle, nCalle, lat, lng)

    codPregunta = data['txt_preguntaseguridad']
    respuestaSeguridad = data['txt_respuestaseguridad']

    RegistrarRespuestaSeguridad(codPregunta, respuestaSeguridad)
    #RegistrarDireccion(region, 1)
    return "OK"

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