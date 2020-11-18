def get_cita():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita
             FROM cita inner join pacientes on pacientes.nombrePaciente = pacientes.nombrePaciente """
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def insertar_cita(cita):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""INSERT INTO cita(id_Paciente_F,fechaCita) VALUES(%s,%s)"""
            cursor.execute(sql, (cita))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM cita"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def editar_cita(cita):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""UPDATE cita SET fechaCita = '%s'"""
            cursor.execute(sql, (cita))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM cita"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def eliminar_cita(cita):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""DELETE FROM cita WHERE idCita = '%s'"""
            cursor.execute(sql, (cita))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM cita"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def buscar_cita_idcita():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita
             FROM cita inner join pacientes on pacientes.nombrePaciente = pacientes.nombrePaciente  WHERE idCita = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def buscar_cita_idpaciente():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita
             FROM cita inner join pacientes on pacientes.nombrePaciente = pacientes.nombrePaciente  WHERE idPaciente_F = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def buscar_cita_fechacita():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita
             FROM cita inner join pacientes on pacientes.nombrePaciente = pacientes.nombrePaciente WHERE fechaCita = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def editar_cita(medico):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""UPDATE cita SET fechaCita = '%s' """
            cursor.execute(sql, (medico))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM cita"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result