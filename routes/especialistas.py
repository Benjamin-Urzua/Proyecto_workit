import base64
from dataclasses import fields
from importlib.resources import as_file
from io import BytesIO
import json, requests
import string
import random
import os
from urllib import response
from sqlalchemy import desc
from werkzeug.datastructures import FileStorage
from flask import Blueprint, make_response, render_template, request, jsonify, send_file, url_for, redirect, session
from sqlalchemy.dialects.mysql import LONGBLOB as blob
from controllers.home import RetornarPerfilEspecialista
from controllers.register import  RegistrarDireccion, SelectRubro
from models.especialista import AutentificarEspecialista, RegistrarEspecialista,  RegistrarPerfilEspecialista, RegistrarProfesion, RegistrarTrabajo

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
        session.pop('nombre')
        session.pop('fotoPerfil')
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
            nombre =str(authResult[3])
            nombre = nombre.split(" ")
            nombre.pop()
            session['nombre'] = nombre[0]
            session['fotoPerfil'] = authResult[4]
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
        session['username'] = run
        session['rol'] = 'especialista'
        session['sesion'] = True
        nombre = nombres.split(" ")
        nombre.pop()
        session['nombre'] = nombre[0]
        return '/especialistas/configPerfil'

@especialistas.route("/especialistas/configPerfil" , methods=['GET', 'POST'])
def configPerfil():
    def generarFn(fnlen):
        return ''.join(random.choice(string.ascii_letters) for i in range(fnlen))
   
    if request.method == 'GET':
        return render_template('especialistas/configPerfil.html')
    else:
        try:
            data = request.form.to_dict()
            images = list(request.files.values())
            
            foto1 = images[0]
            extensionFoto1 = os.path.splitext(foto1.filename)[1]
            print(foto1.filename)
            fnFoto1 =generarFn(10)
            foto1.save(os.path.join('.\static\savedImages', fnFoto1+extensionFoto1))
            foto1 =  fnFoto1+extensionFoto1
            
            foto2 = images[1]
            extensionFoto2 = os.path.splitext(foto2.filename)[1]
            print(foto2.filename)
            fnFoto2 =generarFn(10)
            foto2.save(os.path.join('.\static\savedImages', fnFoto2+extensionFoto2))
            foto2 =  fnFoto2+extensionFoto2
            
            foto3 = images[2]
            extensionFoto3 = os.path.splitext(foto3.filename)[1]
            print(foto3.filename)
            fnFoto3 =generarFn(10)
            foto3.save(os.path.join('.\static\savedImages', fnFoto3+extensionFoto3))
            foto3 =  fnFoto3+extensionFoto3
            
            foto4 = images[3]
            extensionFoto4 = os.path.splitext(foto4.filename)[1]
            print(foto4.filename)
            fnFoto4 =generarFn(10)
            foto4.save(os.path.join('.\static\savedImages', fnFoto4+extensionFoto4))
            foto4 = fnFoto4+extensionFoto4
            
            fotoPerfil = images[4]
            extensionfotoPerfil = os.path.splitext(fotoPerfil.filename)[1]
            print(fotoPerfil.filename)
            fnfotoPerfil =generarFn(10)
            fotoPerfil.save(os.path.join('.\static\savedImages', fnfotoPerfil+extensionfotoPerfil))
            fotoPerfil =  fnfotoPerfil+extensionfotoPerfil
            
            fotoPortada = images[5]
            extensionfotoPortada = os.path.splitext(fotoPortada.filename)[1]
            print(fotoPortada.filename)
            fnfotoPortada =generarFn(10)
            fotoPortada.save(os.path.join('.\static\savedImages', fnfotoPortada+extensionfotoPortada))
            fotoPortada = fnfotoPortada+extensionfotoPortada
            
            
            descripcion = data['txt_descripcion']
            
            listData = list(data)
            contadorTrabajo = 0
            for item in listData:
                if listData.index(item) > 0:
                    if len(item) < 18:
                        lastKey = data[item].replace('txt_', '')
                    else:
                        contadorTrabajo+=1
                        RegistrarTrabajo(lastKey, data[item].replace('txt_', ''), session['username'])
                        #globals()['trabajo{}'.format(contadorTrabajo)] = lastKey
                        #globals()['valorTrabajo{}'.format(contadorTrabajo)] = 
            #run, foto1, foto2, foto3, foto4, fotoPerfil, fotoPortada, descipcion, trabajo1, valorTrabajo1, trabajo2, valorTrabajo2, trabajo3, valorTrabajo3, trabajo4, valorTrabajo4, trabajo5, valorTrabajo5, trabajo6, valorTrabajo6, trabajo7, valorTrabajo7, trabajo8, valorTrabajo8, trabajo9, valorTrabajo9, trabajo10, valorTrabajo10
            
            RegistrarPerfilEspecialista(session['username'],foto1,foto2, foto3, foto4, fotoPerfil, fotoPortada, descripcion)
            
            #print('data: {} \n images: {}'.format(data, images))
            
        except Exception as err:
            print("Algo ha salido mal: {}".format(err))
            return err
        finally:
            session['fotoPerfil'] = fotoPerfil
            return redirect(url_for("especialistas.logout"))

@especialistas.route("/especialistas/perfil" , methods=['GET', 'POST'])
def perfil():
    if 'username' in session:
        username = session['username']
        if request.method == 'GET':
            
            responsePerfil = RetornarPerfilEspecialista(username)
            print(responsePerfil)
            nombres = responsePerfil[0][0]
            apellidos = responsePerfil[0][1]
            profesion = responsePerfil[0][2]
            descripcion = responsePerfil[0][3]         
            
            fotoPerfil = responsePerfil[0][4]
            fotoPortada = responsePerfil[0][5]
            foto1 = responsePerfil[0][6]
            foto2 = responsePerfil[0][7]
            foto3 = responsePerfil[0][8]
            foto4 = responsePerfil[0][9]
                        
            trabajos = []
            valoresTrabajos = []
            for trabajo in responsePerfil:
                trabajos.append(trabajo[10])
                valoresTrabajos.append(trabajo[11])
                
            perfil=[nombres, apellidos, profesion, descripcion, fotoPerfil, fotoPortada, foto1, foto2, foto3, foto4, trabajos, valoresTrabajos]
            print(perfil)
            return render_template('/especialistas/perfil.html', perfil=perfil, zip = zip)
        elif request.method == 'POST':
            data = request.json
            fotoPerfil = data["SendInfo"][0]
            descripcion = data["SendInfo"][1]
            retorno = ActualizarPerfil(username, descripcion, fotoPerfil)
            if len(retorno) > 0:
                return "Perfil Actualizado Exitosamente"
            else:
                return "Algo falló. Su perfil no se ha actualizado"
   