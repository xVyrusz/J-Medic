import mysql.connector
import modulos.db_conexion as conexion

def insertar_cita(idpaciente,fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO cita(idPaciente_F,fechaCita) VALUES(%s,%s)"
        val = (idpaciente,fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM cita")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def editar_cita(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "UPDATE cita SET fechaCita = %s WHERE idCita = %s"
        val = (fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM cita")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def eliminar_cita(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "DELETE FROM cita WHERE idCita = %s"
        val = (fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM cita")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_cita_idcita(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita FROM cita inner join pacientes on pacientes.nombrePaciente = pacientes.nombrePaciente  WHERE idCita = %s"
        val = (fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM cita")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_cita_idpaciente(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita FROM cita inner join pacientes on pacientes.nombrePaciente = pacientes.nombrePaciente  WHERE idPaciente_F = %s"
        val = (fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM cita")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_cita_fechacita(fecha):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "select cita.idCita,cita.idPaciente_F,pacientes.nombrePaciente,pacientes.apellidoPPaciente,pacientes.apellidoMPaciente,cita.fechaCita FROM cita inner join pacientes on pacientes.nombrePaciente = pacientes.nombrePaciente WHERE fechaCita = %s"
        val = (fecha)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM cita")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


