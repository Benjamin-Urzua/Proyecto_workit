from utils.db import engine
from sqlalchemy import text

def RetornarHistorial(run):
    try:
        conexion = engine.raw_connection()
        cursor = conexion.cursor()
        cursor.execute('''call  `sp_retornar_historial`('{run}')'''.format(run=run))
        response = map(list,cursor.fetchall())
    except NameError as err:
        print("Algo ha salido mal: {err}".format(err))
    cursor.close()
    return response

#def RegistrarDireccion(nombreRegion, nombreProvincia, nombreComuna,calle, nCalle, lat, lng, codEstado):
def RegistrarDireccion(nombreRegion, codEstado):
    try:
        conexion = engine.raw_connection()
        cursor = conexion.cursor()
        
        cursor.execute('''call  `sp_ins_region`('{}','{}');'''.format(nombreRegion, codEstado))
        
        # cursor.execute('''call  `sp_generar_direccion`('{nombreRegion}','{nombreProvincia}','{nombreComuna}','{calle}','{nCalle}','{lat}','{lng}');'''.format(nombreRegion=nombreRegion, nombreProvincia=nombreProvincia, nombreComuna=nombreComuna, calle=calle, nCalle=nCalle, lat=lat, lng=lng))
        response = map(list,cursor.fetchall())
        for item in response:
            print(item)
    except NameError as err:
        print("Algo ha salido mal: {err}".format(err))
    cursor.close()
    return response

def Register(run,nombres,apellidos,telefono,correo, contrasena, codDireccion, codRespuesta, fechaNacto, codPerfilCli):
    try:
        conexion = engine.raw_connection()
        cursor = conexion.cursor()
        cursor.execute('''call  `sp_insMod_cliente`('{run}','{nombres}','{apellidos}','{telefono}','{correo}','{contrasena}','{codDireccion}','{codRespuesta}','{fechaNacto}', '{codPerfilCli}')'''.format(run=run,nombre=nombres,apellido=apellidos, telefono = telefono,correo=correo,contrasena=contrasena,codDireccion=codDireccion,codRespuesta=codRespuesta,fechaNacto=fechaNacto,codPerfilCli=codPerfilCli))
        response = map(list,cursor.fetchall())
    except NameError as err:
        print("Algo ha salido mal: {err}".format(err))
    cursor.close()
    return response


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