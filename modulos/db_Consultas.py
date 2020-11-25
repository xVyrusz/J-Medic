import modulos.db_conexion as conexion


def insertar_datos_de_consulta(idmedicos, idpaciente, fecha, motivo):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO datos_de_consulta(idMedicos_F,idPaciente_F,fechaVisita,idMotivo_F) VALUES(%s,%s,%s,%s)"
        val = (idmedicos, idpaciente, fecha, motivo)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def insertar_consulta(idc, pruebas, diagnostico, tratamiento):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO consulta(idConsulta_F,pruebasRealizadas,diagnostico,tratamiento) VALUES(%s,%s,%s,%s)"
        val = (idc, pruebas, diagnostico, tratamiento)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def eliminar_consulta(idc):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "DELETE FROM consulta WHERE idConsulta_F = '{}'".format(idc)
        #val = (idc)
        mycursor.execute(sql)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def eliminar_datos_consulta(idc):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "DELETE FROM datos_de_consulta WHERE idConsulta = '{}'".format(
            idc)
        #val = (idc)
        mycursor.execute(sql)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def editar_datos_de_consulta(idmedicos, idpaciente, fecha, motivo, idConsulta):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "UPDATE datos_de_consulta SET idMedicos_F = %s , idPaciente_F = %s ,fechaVisita =%s  ,idMotivo_F = %s WHERE idConsulta=%s"
        #sql2 ="UPDATE consulta SET pruebasRealizadas = %s , diagnostico= %s ,tratamiento = %s WHERE idConsulta_F=%s"
        val = (idmedicos, idpaciente, fecha, motivo, idConsulta)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def editar_consulta(pruebas, diagnostico, tratamiento, idConsulta):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "UPDATE consulta SET pruebasRealizadas = %s , diagnostico= %s ,tratamiento = %s WHERE idConsulta_F=%s"
        val = (pruebas, diagnostico, tratamiento, idConsulta)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_consulta_id(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F where datos_de_consulta.idConsulta = {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_consulta_medicos(medico):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE medicos.nombreMedico = '{}'".format(
            medico)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_consulta_nombre_paciente(pruebas):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE pacientes.nombrePaciente = '{}' ".format(
            pruebas)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_consulta_motivo(motivo):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.idMotivo_F = '{}'".format(
            motivo)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_consulta_fecha(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.fechaVisita = '{}'".format(
            fecha)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def mostrar_datos_consulta():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        consult = " SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F order by idConsulta DESC"
        mycursor.execute(consult)
        result2 = mycursor.fetchall()
        return result2
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def mostrar_datos_consulta_completa():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        consult = " SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F  order by idConsulta DESC"
        mycursor.execute(consult)
        result3 = mycursor.fetchall()
        return result3
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_consulta_id_2(idn):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if idn:
            consult2 = """
            SELECT datos_de_consulta.idConsulta,medicos.idMedicos,pacientes.idPaciente, motivos_de_consulta.nombreMotivo,datos_de_consulta.fechaVisita,
           consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F where datos_de_consulta.idConsulta= {}""".format(idn)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult2)
        result2 = mycursor.fetchone()
        return result2
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()
