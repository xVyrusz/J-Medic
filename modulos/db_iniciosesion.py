import modulos.db_conexion as conexion


def comprobar_inicio_usuario():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT medicos.usuario FROM mydb.medicos;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()

def comprobar_inicio_contra():
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "SELECT medicos.password FROM mydb.medicos;"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()
