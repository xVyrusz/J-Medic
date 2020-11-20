from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import modulos.db_conexion as conexion
import bcrypt


def insertar_medicos(nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,password):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO medicos(nombreMedico,apellidoPMedico,apellidoMMedico,Cedula,Telefono,id_Turnos_F,usuario,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt(10))
        val = (nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,hashed.decode())
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM medicos")
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()



def buscar_medicos_id(medico):
    result = {}
    connection =  conexion._connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno  
            FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos WHERE idMedicos = '%s'"""
            cursor.execute(sql,(medico))
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def editar_medicos(nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,password):
    result = {}
    connection =  conexion._connect_to_db()
    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""UPDATE medicos SET nombreMedico = '%s' WHERE apellidoPMedico = '%s' WHERE apellidoMMedico ='%s' WHERE Cedula = '%s' WHERE Telefono = '%s' WHERE idTurnos_F = '%s' """
            cursor.execute(sql, (nombre,apellidop,apellidom,cedula,telefono,id_turnos,usuario,password))
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
"""
def tabla (tabla):
    
    #self.table=self.tabla_buscar_medico
    row =0
    sql= "SELECT medicos.idMedicos,nombreMedico,apellidoPMedico,apelLidoMMedico,Cedula,Telefono,turnos.nombreTurno FROM medicos inner join turnos on medicos.idTurnos_F=turnos.idTurnos WHERE idMedicos = '%s'"
    query =QSqlQuery(sql)
    while query.next():
        self.table.insertRow(row)
        idMedicos=self.tabla_buscar_medico(str(query.value(0)))
        nombreMedico=self.tabla_buscar_medico(str(query.value(1)))
        apellidoPMedico=self.tabla_buscar_medico(str(query.value(2)))
        apellidoMMedico=self.tabla_buscar_medico(str(query.value(3)))
        Cedula=self.tabla_buscar_medico(str(query.value(4)))
        Telefono=self.tabla_buscar_medico(str(query.value(5)))
        idTurnos_F=self.tabla_buscar_medico(str(query.value(6)))
        self.table.setItem(row, 0, idMedicos)
        self.table.setItem(row, 1, nombreMedico)
        self.table.setItem(row, 2, apellidoPMedico)
        self.table.setItem(row, 3, apellidoMMedico)
        self.table.setItem(row, 4, Cedula)
        self.table.setItem(row, 5, Telefono)
        self.table.setItem(row, 6, idTurnos_F)
        row = row+1
"""