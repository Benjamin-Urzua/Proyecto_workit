import json, requests
from datetime import datetime
from msilib.schema import Billboard
from flask import Blueprint, make_response, render_template, request, jsonify, url_for, redirect, session
from controllers.home import RetornarPerfilCliente
from models.cliente import  ActualizarPerfil, AutentificarCliente, EliminarCuenta, RegistrarCliente, RegistrarDireccion, RegistrarPerfilCliente, RegistrarRespuestaSeguridad,  RetornarHistorial
from controllers.register import  SelectPreguntas

clientes = Blueprint('clientes', __name__)
    
@clientes.route("/clientes/perfil" , methods=['GET', 'POST'])
def perfil():
    if 'username' in session:
        username = session['username']
        if request.method == 'GET':
            perfil = RetornarPerfilCliente(username)[0]
            print(perfil)
            return render_template('/clientes/perfil.html', perfil = perfil)
        elif request.method == 'POST':
            data = request.json
            fotoPerfil = data["SendInfo"][0]
            descripcion = data["SendInfo"][1]
            retorno = ActualizarPerfil(username, descripcion, fotoPerfil)
            if len(retorno) > 0:
                return "Perfil Actualizado Exitosamente"
            else:
                return "Algo falló. Su perfil no se ha actualizado"
   

@clientes.route("/clientes/logout", methods=['POST', 'GET'])
def logout():
    if 'username' in session:
        session.pop('username')
        msj = "Sesion cerrada"
    return render_template('home.html', msj = msj)

@clientes.route("/clientes/login", methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return redirect(url_for('index.home'))
    else:
        return render_template('clientes/login.html')
  
@clientes.route("/clientes/login/autentificacion", methods=['GET', 'POST'])
def autentificar():
    try:
        data = request.form.to_dict()
        authResult = AutentificarCliente(data['txt_correo'], data['txt_contrasena'])
        retorno = {}
        if authResult[1] == 1:
            session['username'] = authResult[2]
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
        #return print(AutentificarCliente(data['txt_correo', data['txt_contrasena']]))
    '''
    else: 
        retorno = {"Codigo":3, "Msj":"Ya existe una sesión abierta.", "Redirect": "/"}
        return retorno
    '''    

@clientes.route("/clientes/historial")
def retornar_historial():
    if 'username' in session:
        run = session['username']
        historial = RetornarHistorial(run)
        if historial[0][1] == -1:
            msj = historial[0][0]
            code = -1
            return render_template("clientes/historial.html", historial = historial, run = run, msj = msj, code = code)
        else:
            return render_template("clientes/historial.html", historial = historial, run = run, code = 1)
    else:
        return redirect(url_for('index.home'))
    

@clientes.route("/clientes/registrarse", methods=['POST', 'GET'])
def registrarse():
    preguntas = SelectPreguntas()
    return render_template('/clientes/register.html', preguntas = preguntas)
    
@clientes.route("/clientes/registrarse/guardar", methods=['GET', 'POST'])
def guardar_registro():
    try:
        data = request.form.to_dict()
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

        codPregunta = int(data['txt_preguntaseguridad'].replace('"', ""))
        respuestaSeguridad = data['txt_respuestaseguridad']


        RegistrarRespuestaSeguridad(codPregunta, respuestaSeguridad)
        RegistrarPerfilCliente()
        
        run = data['txt_run']
        nombres = data['txt_nombres']
        apellidos = data['txt_apellidos']
        telefono = data['txt_telefono']
        correo =  data['txt_correo']
        contrasena = data['txt_contrasena1']
        fechaNacto = data['txt_fechanacto']
        print(RegistrarCliente(run, nombres, apellidos, telefono, correo, contrasena, fechaNacto))
    except Exception as err:
            print("Algo ha salido mal: {}".format(err))
    finally:
        return '/'

@clientes.route("/clientes/eliminarCuenta" ,methods=['GET', 'POST'])
def eliminar():
    if 'username' in session:
        try:
            data = request.form.to_dict()
            authResult = AutentificarCliente(data['txt_correo'], data['txt_contrasena'])
            print('authResult: {}'.format(authResult))
            print('session: {}'.format(type(session['username'])))
            retorno = {}
            if authResult[1] == 1:
                delResult = EliminarCuenta(session['username'])
                print('delResult: {}'.format(delResult))
                if delResult[1] == 1 or delResult[1] == 2 :
                    session.pop('username')
                    retorno =  {
                        "Msj": "Su cuenta se ha borrado",
                        "Codigo": 1,
                        "Redirect": "/" 
                    }
                else:
                    retorno =  {
                        "Msj": "Algo ha salido mal. Su cuenta sigue vigente",
                        "Codigo": -1,
                        "Redirect": "" 
                    }
            else:
                retorno = {
                    "Msj": "Credenciales incorrectas",
                    "Codigo": -2,
                    "Redirect": "" 
                }
        except Exception as err:
                print("Algo ha salido mal: {}".format(err))
        finally:
            return retorno