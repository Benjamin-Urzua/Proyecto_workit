from utils.db import db
from sqlalchemy import text

def SelectPreguntas():
    query = db.engine.execute(text("SELECT * FROM `tb_preguntasseguridad`"))
    response = map(list,query)
    return response