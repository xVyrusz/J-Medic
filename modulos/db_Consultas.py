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
        mycursor.execute("SELECT * FROM datos_de_consulta")
        result = mycursor.fetchall()
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
        mycursor.execute("SELECT * FROM consulta")
        result = mycursor.fetchall()
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
        mycursor.execute("SELECT * FROM datos_de_consulta")
        result = mycursor.fetchall()
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
        mycursor.execute("SELECT * FROM datos_de_consulta")
        result = mycursor.fetchall()
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
        mycursor.execute("SELECT * FROM consulta")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_consulta_id(pruebas):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_Finner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPacienteinner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_Finner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE consulta.idConsulta_F = %s"
        val = (pruebas)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM datos_de_consulta")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_consulta_medicos(pruebas):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_Finner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPacienteinner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_Finner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE medicos.nombreMedico = %s"
        val = (pruebas)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM datos_de_consulta")
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
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita, motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_Finner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPacienteinner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE pacientes.nombrePaciente = %s"
        val = (pruebas)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM datos_de_consulta")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_consulta_motivo(pruebas):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_Finner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPacienteinner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_Finner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.idMotivo_F = %s"
        val = (pruebas)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM datos_de_consulta")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_consulta_fecha(pruebas):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_Finner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPacienteinner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_Finner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F WHERE datos_de_consulta.fechaVisita = %s"
        val = (pruebas)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM datos_de_consulta")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()
