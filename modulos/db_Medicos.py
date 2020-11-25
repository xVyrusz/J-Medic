import modulos.db_conexion as conexion
from PyQt5.QtWidgets import QMessageBox
#import bcrypt


def insertar_medicos(nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,password):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO medicos(nombreMedico,apellidoPMedico,apellidoMMedico,Cedula,Telefono,idTurnos_F,usuario,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        #hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(10))
        if id_turnos=="Matutino":
            id_turnos = 1
        elif id_turnos=="Vespertino":
            id_turnos = 2
        else:
            pass
        val = (nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,password)
        #val = (nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,hashed.decode())

        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM medicos")
        result = mycursor.fetchall()

        result = 1
        return result
    except:
        QMessageBox.information(self, "Error al guardar los datos", "Su informacion no se ha guardado", QMessageBox.Discard)
    finally:
        mydb.close()
        mycursor.close()


def buscar_medicos_id(id):
    mydb = conexion.conexion()
    mycursor = mydb.cursor()
    try:
        if id:
            consult = """
            SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno 
            FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos
             WHERE idMedicos= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except expression as identifier:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


