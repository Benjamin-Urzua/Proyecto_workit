from utils.db import engine
from sqlalchemy import text

def RetornarHistorial(run):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_retornar_historial', [run])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)

def RegistrarRespuestaSeguridad(codPregunta, respuesta):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_generar_preguntaRespuesta', [codPregunta, respuesta])        
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return response

def RegistrarPerfilCliente():
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_ins_perfilcliente', ["", ""])        
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return response

def RegistrarCliente(run,nombres,apellidos,telefono,correo, contrasena, fechaNacto):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_ins_cliente', [run, nombres, apellidos, telefono, correo, contrasena, fechaNacto])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)

def AutentificarCliente(correo, contrasena):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_autentificar_cliente', [correo, contrasena])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)[0]

def EliminarCuenta(run):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_eliminarCliente', [run])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)[0] 

def ActualizarPerfil(run, descripcion, fotoPerfil):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_update_perfilCliente', [run, descripcion, fotoPerfil])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)[0] 

'''
class Cliente(db.model):
    __tablename__="tb_cliente"
    run=db.Column(db.String(10), primary_key=True, null=False),
    nombres=db.Column(db.String(100), null=False),
    apellidos=db.Column(db.String(100),  null=False),
    telefono=db.Column(db.Integer(9),  null=False),
    correo=db.Column(db.String(60),  null=False),
    contrasena=db.Column(db.String(60),  null=False),
    codDireccion=db.Column(db.Integer(11),   null=False), #poner foreign key luego
    codRespuesta=db.Column(db.Integer(11),   null=False), #poner foreign key luego
    fechaNacto=db.Column(db.Date,   null=False)
    codPerfilCli=db.Column(db.Integer(11), null=False)
    
    def __init__(self, run, nombres, apellidos, telefono, correo, contrasena, codDireccion, codRespuesta, fechaNacto, codPerfilCli):
        self.run = run
        self.nombres = nombres
        self.apellidos = apellidos
        self. telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.codDireccion = codDireccion
        self.codRespuesta = codRespuesta
        self.fechaNacto = fechaNacto
        self.codPerfilCli = codPerfilCli
        
class Especialista(db.model):
    __tablename__="tb_especialista"
    run=db.Column(db.String(10), primary_key=True, null=False),
    nombres=db.Column(db.String(100), null=False),
    apellidos=db.Column(db.String(100),  null=False),
    telefono=db.Column(db.Integer(9),  null=False),
    correo=db.Column(db.String(60),  null=False),
    contrasena=db.Column(db.String(60),  null=False),
    codDireccion=db.Column(db.Integer(11),   null=False), #poner foreign key luego
    codProfesion=db.Column(db.Integer(11),   null=False), #poner foreign key luego
    cedulaFrontal=db.Column(db.String(2000),  null=False),
    cedulaTrasera=db.Column(db.String(2000),  null=False),
    certAntecedentes=db.Column(db.String(2000),  null=False),
    codPerfilEsp =db.Column(db.Integer(11),  null=False),
    tituloProfesional=db.Column(db.String(2000),  null=False),
    disponibilidad=db.Column(db.Boolean,  null=False),
    
    def __init__(self, run, nombres, apellidos, telefono, correo, contrasena, codDireccion, codProfesion, cedulaFrontal, cedulaTrasera,certAntecedentes,codPerfilEsp,tituloProfesional,disponibilidad):
        self.run = run
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.codDireccion = codDireccion
        self.codProfesion = codProfesion
        self.cedulaFrontal = cedulaFrontal
        self.cedulaTrasera = cedulaTrasera
        self.certAntecedentes = certAntecedentes
        self.codPerfilEsp = codPerfilEsp
        self.tituloProfesional = tituloProfesional
        self.disponibilidad = disponibilidad

class Direccion(db.model):
    __tablename__="tb_direccion"
    codDireccion=db.Column(db.Integer(11),  primary_key=True, null=False)
    nombres=db.Column(db.String(100), null=False),
    nCalle=db.Column(db.String(20), null=False),
    lat=db.Column(db.String(150), null=False),
    long=db.Column(db.String(150), null=False),
    codComuna=db.Column(db.Integer(11),   null=False), #poner foreign key luego
    
    def __init__(self, codDireccion, nombres, nCalle, lat, long, codComuna):
        self.codDireccion = codDireccion
        self.nombres = nombres
        self.nCalle = nCalle
        self.lat = lat
        self.long = long
        self.codComuna = codComuna
        
class Comuna(db.model):
    __tablename__="tb_direccion"
    codComuna = db.Column(db.Integer(11) ,  primary_key=True, null=False)
    nombreComuna  = db.Column(db.String(100), null=False)
    codProvincia  = db.Column(db.Integer(11) , null=False)
    
    def __init__(self, codComuna, nombreComuna, codProvincia):
        self.codComuna = codComuna
        self. nombreComuna = nombreComuna
        self.codProvincia = codProvincia
        
class Provincia(db.model):
    __tablename__="tb_provincia"
    codProvincia = db.Column(db.Integer(11) ,  primary_key=True, null=False)
    nombreProvincia  = db.Column(db.String(100), null=False)
    codRegion  = db.Column(db.String(4) , null=False)
    
    def __init__(self, codProvincia, nombreProvincia, codRegion):
        self.codProvincia = codProvincia
        self. nombreProvincia = nombreProvincia
        self.codRegion = codRegion
        
class Provincia(db.model):
    __tablename__="tb_region"
    codRegion = db.Column(db.String(4) ,  primary_key=True, null=False)
    nombreRegion  = db.Column(db.String(100), null=False)
    
    def __init__(self, codRegion, nombreRegion):
        self.codRegion = codRegion
        self. nombreRegion = nombreRegion
        
class EstadoTrabajo(db.model):
    __tablename__="tb_estadotrabajo"
    codEstadoTrabajo = db.Column(db.Integer(11) ,  primary_key=True, null=False)
    estado  = db.Column(db.String(20), null=False)
    
    def __init__(self, codEstadoTrabajo, estado):
        self.codEstadoTrabajo = codEstadoTrabajo
        self. estado = estado
        
class DetalleOrdenServicio(db.model):
    __tablename__="tb_detalleordenservicio"
    codDetalleOrden = db.Column(db.Integer(11) ,  primary_key=True, null=False)
    codTrabajoEspecialista = db.Column(db.Integer(11) , null=False)
    codRubro = db.Column(db.Integer(11) , null=False)
    cantServicios = db.Column(db.Integer(11) , null=False)
    
    def __init__(self, codDetalleOrden, codTrabajoEspecialista,codRubro,cantServicios):
        self.codDetalleOrden = codDetalleOrden
        self. codTrabajoEspecialista = codTrabajoEspecialista
        self. codRubro = codRubro
        self. cantServicios = cantServicios
'''