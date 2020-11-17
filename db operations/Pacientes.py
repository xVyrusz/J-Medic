#from  import _connect_to_db


def get_pacientes():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre """
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

#paciente es el parametro
def insertar_pacientes(paciente):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""INSERT INTO pacientes(nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,idTipo_Sangre) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (paciente))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM pacientes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def editar_pacientes(paciente):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""UPDATE pacientes SET nombrePaciente = '%s' WHERE apellidoPPaciente = '%s' WHERE apellidoMPaciente ='%s' WHERE sexoPaciente = '%s' WHERE estaturaPaciente = '%s' WHERE edadPaciente = '%s' WHERE telefonoPaciente = '%s' WHERE alergiasPaciente = '%s' WHERE idTipo_Sangre = '%s'"""
            cursor.execute(sql, (paciente))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM pacientes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def buscar_pacientes_id():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT * FROM pacientes WHERE idPaciente = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def buscar_pacientes_nombre():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT * FROM pacientes WHERE nombrePaciente = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

insertar = insertar_pacientes()
print(insertar)