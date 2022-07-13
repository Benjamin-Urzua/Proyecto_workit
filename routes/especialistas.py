from dataclasses import fields
import json, requests
import numpy as np
from werkzeug.datastructures import FileStorage
from flask import Blueprint, make_response, render_template, request, jsonify, url_for, redirect, session
from sqlalchemy.dialects.mysql import BLOB as blob
from controllers.home import RetornarPerfilEspecialista
from controllers.register import  RegistrarDireccion, SelectRubro
from models.especialista import AutentificarEspecialista, RegistrarEspecialista, RegistrarPerfilEspecialista, RegistrarProfesion

especialistas = Blueprint('especialistas', __name__)

@especialistas.route("/especialistas/registrarse", methods=['POST', 'GET'])
def registrarse():
    rubros = SelectRubro()
    return render_template('/especialistas/register.html' , rubros = rubros)

@especialistas.route("/especialistas/login", methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('index.home'))
    else:
        return render_template('especialistas/login.html')
  
@especialistas.route("/especialistas/logout", methods=['POST', 'GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        session.pop('rol')
        session['sesion'] = False
        return redirect(url_for('index.home'))

@especialistas.route("/especialistas/login/autentificacion", methods=['GET', 'POST'])
def autentificar():
    try:
        data = request.form.to_dict()
        authResult = AutentificarEspecialista(data['txt_correo'], data['txt_contrasena'])
        retorno = {}
        if authResult[1] == 1:
            session['username'] = authResult[2]
            session['rol'] = 'especialista'
            session['sesion'] = True
            retorno = {
                "Msj": "Sesión iniciada correctamente",
                "Codigo": 1,
                "Redirect": "/" 
            }
        else:
            retorno = {
                "Msj": "Contraseña y/o correo incorrectos",
                "Codigo": -1,
                "Redirect": "" 
            }
    except Exception as err:
            print("Algo ha salido mal: {}".format(err))
    finally:
        return retorno

@especialistas.route("/especialistas/registrarse/guardar", methods=['GET', 'POST'])
def guardar_registro():
    try:
        data = request.form.to_dict()
        images = list(request.files.values())
        
        
        imgCedula = blob(images[0].read())#Leo el blob de la imagen para subirla
        
        imgTitProfesional = blob(images[1].read())
        
        imgCertResidencia = blob(images[2].read())
        
        imgCertAntecedentes = blob(images[3].read())
        
        calleNum = data['txt_direccion'].split(' ')
        nCalle = calleNum[-1]
        calleNum.pop()
        calle = '+'
        calle = calle.join(calleNum)
        
        regionResponse = requests.get('https://apis.digital.gob.cl/dpa/regiones/{}'.format(data['combo_region']), params=[('q', 'requests+language:python')], headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
        provinciaResponse = requests.get('https://apis.digital.gob.cl/dpa/provincias/{}'.format(data['combo_provincia']), params=[('q', 'requests+language:python')], headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
        comunaResponse = requests.get('https://apis.digital.gob.cl/dpa/comunas/{}'.format(data['combo_comuna']), params=[('q', 'requests+language:python')], headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
        
        obtenerRegion = json.loads(regionResponse.text) #Recibo respuesta Region de la api
        region = obtenerRegion["nombre"].replace(' ', '+') #Obtengo solo el nombre
        
        obtenerProvincia = json.loads(provinciaResponse.text) #Recibo respuesta Provincia de la api
        provincia = obtenerProvincia["nombre"].replace(' ', '+') #Obtengo solo el nombre
        
        obtenerComuna = json.loads(comunaResponse.text) #Recibo respuesta Comuna de la api
        comuna = obtenerComuna["nombre"].replace(' ', '+') #Obtengo solo el nombre
        
        mapsResponse = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}+{}+,+{}+,+{}+,+{}+,+Chile&key=AIzaSyBwOsP73t_qgFi88Wa374i--YZ1ExOLpqQ'.format(nCalle, calle, comuna, provincia, region)) #Obtengo lat y lng por medio de google maps
        maps = json.loads(mapsResponse.text)
       
        calle = calle.replace('+', ' ') 
        region = region.replace('+', ' ') 
        provincia = provincia.replace('+', ' ') 
        comuna = comuna.replace('+', ' ') 
        lat = maps["results"][0]["geometry"]["location"]["lat"]
        lng = maps["results"][0]["geometry"]["location"]["lng"]
            
        RegistrarDireccion(region, provincia, comuna,calle, nCalle, lat, lng)
        
        nombreProfesion = data["txt_profesion"]
        codRubro = data["txt_rubro"]
        
        print(list(RegistrarProfesion(nombreProfesion,codRubro)))
        print(list(RegistrarPerfilEspecialista()))
        
        run = data['txt_run']
        nombres = data['txt_nombres']
        apellidos = data['txt_apellidos']
        telefono = data['txt_telefono']
        correo =  data['txt_correo']
        contrasena = data['txt_contrasena1']
        
        print(RegistrarEspecialista(run, nombres, apellidos, telefono, correo, contrasena, imgCedula.length, imgCertAntecedentes.length, imgCertResidencia.length, imgTitProfesional.length))
        
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        return '/'

@especialistas.route("/especialistas/perfil" , methods=['GET', 'POST'])
def perfil():
    if 'username' in session:
        username = session['username']
        if request.method == 'GET':
            perfil = RetornarPerfilEspecialista(username)[0]
            print(perfil)
            return str(perfil)
            #return render_template('/especialistas/perfil.html', perfil = perfil)
        elif request.method == 'POST':
            data = request.json
            fotoPerfil = data["SendInfo"][0]
            descripcion = data["SendInfo"][1]
            retorno = ActualizarPerfil(username, descripcion, fotoPerfil)
            if len(retorno) > 0:
                return "Perfil Actualizado Exitosamente"
            else:
                return "Algo falló. Su perfil no se ha actualizado"
   