

def get_datos_consulta():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f""" SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def insertar_datos_consulta(consulta):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""INSERT INTO datos_de_consulta(idMedicos_F,idPaciente_F,fechaVisita,idMotivo_F) VALUES(%s,%s,%s,%s)"""
            cursor.execute(sql, (consulta))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM datos_de_consulta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def get_consulta():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f""" SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVista,motivos_de_consulta.nombreMotivo
            consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento
            FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPacientes_F
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F
            WHERE datos_de_consulta.idPaciente_F=datos_de_consulta.idConsulta """
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def eliminar_consulta(consulta):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""DELETE FROM datos_de_consulta WHERE idConsulta  = '%s'"""
            cursor.execute(sql, (consulta))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM datos_de_consulta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def editar_datos_consultas(consulta):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""UPDATE datos_de_consulta SET idMedicos_F = '%s' WHERE idPaciente_F = '%s' WHERE fechaVisita ='%s' WHERE idMotivo_F = '%s' """
            cursor.execute(sql, (consulta))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM datos_de_consulta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def editar_consulta(consulta):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""UPDATE consulta SET pruebasRealizadas = '%s' WHERE diagnostico = '%s' WHERE tratamiento ='%s'  """
            cursor.execute(sql, (consulta))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM consulta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result



def buscar_consulta_id():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE consulta.idConsulta_F = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def buscar_consulta_medico():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE medicos.idMedicos = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def buscar_consulta_nombre():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE pacientes.nombrePaciente = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def buscar_consulta_motivo():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.idMotivo_F = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result


def buscar_consulta_fecha():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.fechaVisita = '%s'"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result