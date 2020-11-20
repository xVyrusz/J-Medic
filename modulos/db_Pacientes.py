import mysql.connector
import modulos.db_conexion as conexion

def insertar_pacientes(nombre,apellidop,apellidom,sexo,peso,estatura,edad,telefono,alergias,sangre):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO pacientes (nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,alergiasPaciente,idTipo_Sangre_F) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (nombre,apellidop,apellidom,sexo,peso,estatura,edad,telefono,alergias,sangre)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM pacientes")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def buscar_pacientes_id(nombre):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre WHERE pacientes.idPaciente = %s"
        val = (nombre)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM pacientes")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_pacientes_nombre(nombre):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre WHERE  pacientes.nombrePaciente  = %s"
        val = (nombre)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM pacientes")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

