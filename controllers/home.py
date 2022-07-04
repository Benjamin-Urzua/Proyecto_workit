from utils.db import engine

def RetornarPerfilCliente(run):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_retornar_perfilCliente', [run])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
    return list(response)