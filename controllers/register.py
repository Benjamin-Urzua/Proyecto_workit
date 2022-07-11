from utils.db import engine
from sqlalchemy import text


def SelectPreguntas():
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.execute('''SELECT * FROM `tb_preguntasseguridad`''')
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
    return response

def SelectRubro():
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.execute('''SELECT codRubro, nombreRubro FROM `tb_rubro`''')
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
    return list(response)

def RetornarRegion(nombreRegion):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.execute('''select codRegion from tb_region where nombreRegion = '{}';'''.format(nombreRegion))
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
    return response


