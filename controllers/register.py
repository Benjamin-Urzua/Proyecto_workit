from utils.db import db
from sqlalchemy import text

def SelectPreguntas():
    query = db.engine.execute(text("SELECT * FROM `tb_preguntasseguridad`"))
    response = map(list,query)
    return response

def RetornarRegion(nombreRegion):
    query = db.engine.execute(text("select * from tb_region where nombreRegion = '{}';".format(nombreRegion)))
    response = map(list,query)
    return response
