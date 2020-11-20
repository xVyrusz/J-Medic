import mysql.connector
import modulos.db_conexion as conexion

def insertar_datos_de_consulta(idmedicos,idpaciente,fecha,motivo):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO datos_de_consulta(idMedicos_F,idPaciente_F,fechaVisita,idMotivo_F) VALUES(%s,%s,%s,%s)"
        val = (idmedicos,idpaciente,fecha,motivo)
        mycursor.execute(sql, val)
        mydb.commit()
        result =1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()
def insertar_consulta(pruebas,diagnostico,tratamiento):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO consulta(pruebasRealizadas,diagnostico,tratamiento) VALUES(%s,%s,%s)"
        val = (pruebas,diagnostico,tratamiento)
        mycursor.execute(sql, val)
        mydb.commit()
        result =1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()
def eliminar_consulta(pruebas):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "DELETE FROM datos_de_consulta WHERE idConsulta  = %s"
        val = (pruebas)
        mycursor.execute(sql, val)
        mydb.commit()
        result =1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def editar_datos_de_consulta(idmedicos,idpaciente,fecha,motivo):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "UPDATE datos_de_consulta SET idMedicos_F = %s , idPaciente_F = %s ,fechaVisita =%s  ,idMotivo_F = %s WHERE idConsulta=%s"
        val = (idmedicos,idpaciente,fecha,motivo)
        mycursor.execute(sql, val)
        mydb.commit()
        result =1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def editar_consulta(pruebas,diagnostico,tratamiento):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "UPDATE datos_de_consulta SET idMedicos_F = %s , idPaciente_F = %s ,fechaVisita =%s  ,idMotivo_F = %s WHERE idConsulta=%s"
        val = (pruebas,diagnostico,tratamiento)
        mycursor.execute(sql, val)
        mydb.commit()
        result =1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()





def buscar_consulta_id(id):
    mydb = conexion.conexion()
    mycursor = mydb.cursor()
    try:
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
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE medicos.nombreMedico = '{}'".format(medico)
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
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE pacientes.nombrePaciente = '{}' ".format(pruebas)
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
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.idMotivo_F = '{}'".format(motivo)
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
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.fechaVisita = '{}'".format(fecha)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()