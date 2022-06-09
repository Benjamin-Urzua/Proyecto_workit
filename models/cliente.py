from utils.db import db
from sqlalchemy.orm import declarative_base, relationship

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
    fotoPerfil=db.Column(db.String(2000))
    
    def __init__(self, run, nombres, apellidos, telefono, correo, contrasena, codDireccion, codRespuesta, fechaNacto, fotoPerfil):
        self.run = run
        self.nombres = nombres
        self.apellidos = apellidos
        self. telefono = telefono
        self.correo = correo
        self.contrasena = contrasena
        self.codDireccion = codDireccion
        self.codRespuesta = codRespuesta
        self.fechaNacto = fechaNacto
        self.fotoPerfil = fotoPerfil

class Direccion (db.model):
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