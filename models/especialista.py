from utils.db import engine

def RegistrarProfesion(nombreProfesion, codRubro):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_generar_profesion', [nombreProfesion, codRubro])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)

def RegistrarPerfilEspecialista(run,foto1,foto2, foto3, foto4, fotoPerfil, fotoPortada, descripcion ):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_ins_perfilEspecialista', [run,foto1,foto2, foto3, foto4, fotoPerfil, fotoPortada, descripcion ])        
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return response
    
def RegistrarTrabajo(trabajo, valorTrabajo, run):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_ins_trabajos', [trabajo, valorTrabajo, run])        
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return response

def RegistrarEspecialista(run,nombres,apellidos,telefono,correo, contrasena, cedulaIdentidad, certAntecedentes, certResidencia, tituloProfesional):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_ins_especialista', [run, nombres, apellidos, telefono, correo, contrasena, cedulaIdentidad,certAntecedentes, certResidencia,  tituloProfesional])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)
    
def AutentificarEspecialista(correo, contrasena):
    conexion = engine.raw_connection()
    try:
        cursor = conexion.cursor()
        cursor.callproc('sp_autentificar_especialista', [correo, contrasena])
        response = map(list,cursor.fetchall())
        cursor.close()
        conexion.commit()
    except Exception as err:
        print("Algo ha salido mal: {}".format(err))
    finally:
        conexion.close()
        return list(response)[0]
    
