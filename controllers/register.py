from utils.db import engine
from sqlalchemy import text


def SelectPreguntas():
    conexion = engine.raw_connection()
    cursor = conexion.cursor()
    cursor.execute('''SELECT * FROM `tb_preguntasseguridad`''')
    response = map(list,cursor.fetchall())
    cursor.close()
    return response

def RetornarRegion(nombreRegion):
    conexion = engine.raw_connection()
    cursor = conexion.cursor()
    cursor.execute('''select codRegion from tb_region where nombreRegion = '{}';'''.format(nombreRegion))
    response = map(list,cursor.fetchall())
    cursor.close()
    return response


