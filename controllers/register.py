from utils.db import db
from sqlalchemy import text

def SelectPreguntas():
    query = db.engine.execute(text("SELECT * FROM `tb_preguntasseguridad`"))
    response = map(list,query)
    return response

def RetornarRegion(nombreRegion):
    query = db.engine.execute(text("select codRegion from tb_region where nombreRegion = '{}';".format(nombreRegion)))
    response = map(list,query)
    return response

def RetornarProvincia(nombreProvincia):
    query = db.engine.execute(text("select codProvincia from tb_provincia where nombreProvincia = '{}';".format(nombreProvincia)))
    response = map(list,query)
    return response

def RetornarComuna(nombreComuna):
    query = db.engine.execute(text("select codComuna from tb_comuna where nombreComuna = '{}';".format(nombreComuna)))
    response = map(list,query)
    return response
