


def get_medicos():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT * FROM medicos"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def insertar_medicos(medico):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""INSERT INTO medicos(nombreMedico,apellidoPMedico,apellidoMMedico,Cedula,Telefono,id_Turnos_F) VALUES(%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (medico))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM medicos"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def buscar_medicos_id():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT * FROM medicos WHERE idMedicos = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def editar_medicos(medico):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""UPDATE medicos SET nombreMedico = '%s' WHERE apellidoPMedico = '%s' WHERE apellidoMMedico ='%s' WHERE Cedula = '%s' WHERE Telefono = '%s' WHERE idTurnos_F = '%s' """
            cursor.execute(sql, (medico))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM medicos"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result