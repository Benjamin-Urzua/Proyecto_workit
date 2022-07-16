import base64
from dataclasses import fields
import json, requests
from urllib import response
from sqlalchemy import desc
from werkzeug.datastructures import FileStorage
from flask import Blueprint, make_response, render_template, request, jsonify, url_for, redirect, session
from sqlalchemy.dialects.mysql import LONGBLOB as blob
from controllers.home import RetornarPerfilEspecialista
from controllers.register import  RegistrarDireccion, SelectRubro
from models.especialista import AutentificarEspecialista, RegistrarEspecialista, RegistrarFotosTrabajos, RegistrarPerfilEspecialista, RegistrarProfesion, RegistrarTrabajo

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
        return '/especialistas/configPerfil'

@especialistas.route("/especialistas/configPerfil" , methods=['GET', 'POST'])
def configPerfil():
    if request.method == 'GET':
        return render_template('especialistas/configPerfil.html')
    else:
        try:
            data = request.form.to_dict()
            images = list(request.files.values())
            
            foto1 = blob(images[0].read()).length#Leo el blob de la imagen para subirla
            foto2 = blob(images[1].read()).length
            foto3 = blob(images[2].read()).length
            foto4 = blob(images[3].read()).length
            fotoPerfil = blob(images[4].read()).length
            fotoPortada = blob(images[5].read()).length
            
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
            
            RegistrarFotosTrabajos(foto1, foto2, foto3, foto4)
            RegistrarPerfilEspecialista(descripcion, fotoPerfil, fotoPortada,session['username'])
            
            #print('data: {} \n images: {}'.format(data, images))
            
        except Exception as err:
            print("Algo ha salido mal: {}".format(err))
        finally:
            return '/'

@especialistas.route("/especialistas/perfil" , methods=['GET', 'POST'])
def perfil():
    if 'username' in session:
        username = session['username']
        if request.method == 'GET':
            
            responsePerfil = RetornarPerfilEspecialista(username)
            
            nombres = responsePerfil[0][0]
            apellidos = responsePerfil[0][1]
            profesion = responsePerfil[0][2]
            descripcion = responsePerfil[0][3]
            
            fotoPerfil = base64.b64encode(responsePerfil[0][4])
            def is64(coso):
                try:
                    return base64.b64encode(base64.b64decode(coso)) == coso
                except Exception:
                    return False
                
            
            fotoPerfil = base64.b64encode(responsePerfil[0][4].decode("UTF-8", "ignore").encode("ASCII", "ignore"))
            fotoPortada = base64.b64encode(responsePerfil[0][5].decode("UTF-8", "ignore").encode("ASCII", "ignore"))
            foto1 = base64.b64encode(responsePerfil[0][6].decode("UTF-8", "ignore").encode("ASCII", "ignore"))
            foto2 = base64.b64encode(responsePerfil[0][7].decode("UTF-8", "ignore").encode("ASCII", "ignore"))
            foto3 = base64.b64encode(responsePerfil[0][8].decode("UTF-8", "ignore").encode("ASCII", "ignore"))
            foto4 = base64.b64encode(responsePerfil[0][9].decode("UTF-8", "ignore").encode("ASCII", "ignore"))
            
            print(json.detect_encoding(fotoPerfil))
            
            trabajos = []
            valoresTrabajos = []
            for trabajo in responsePerfil:
                trabajos.append(trabajo[10])
                valoresTrabajos.append(trabajo[11])
                
            perfil=[nombres, apellidos, profesion, descripcion, fotoPerfil, fotoPortada, foto1, foto2, foto3, foto4, trabajos, valoresTrabajos]
            '''
            especialista = responsePerfil[0][0]
            rubro = responsePerfil[0][1]
            descripcion = responsePerfil[0][2]
            
            fotoPerfil = FileStorage
            fotoPerfil.stream = responsePerfil[0][3]
            fotoPerfil.stream = base64.b64encode(fotoPerfil.stream)

            fotoPortada = FileStorage
            fotoPortada.stream = responsePerfil[0][4]
            fotoPortada.stream = base64.b64encode(fotoPortada.stream)
            #fotoPortada = responsePerfil[0][4]
            trabajos = []
            valoresTrabajos = []
            
            
            for trabajo in responsePerfil:
                trabajos.append(trabajo[5])
                valoresTrabajos.append(trabajo[6])
            
            foto1 = FileStorage
            foto1.stream = responsePerfil[0][7]
            foto1.stream = base64.b64encode(foto1.stream)
            
            foto2 = FileStorage
            foto2.stream = responsePerfil[0][8]
            foto2.stream  = base64.b64encode(foto2.stream)
            
            foto3 = FileStorage
            foto3.stream = responsePerfil[0][9]
            foto3.stream = base64.b64encode(foto3.stream)
            
            foto4 = FileStorage
            foto4.stream = responsePerfil[0][10]
            foto4.stream = base64.b64encode(foto4.stream)
            
            
            perfil=[especialista, rubro, descripcion, fotoPerfil, fotoPortada, trabajos, valoresTrabajos, foto1, foto2, foto3, foto4]
            '''
            
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
   