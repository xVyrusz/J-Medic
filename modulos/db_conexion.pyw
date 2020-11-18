import pymysql.cursors

HOST ='localhost'
DB_USER = 'root'
PASSWORD = 'root'
DB = 'mydb'
CHARSET = 'utf8'
CURSORCLASS = pymysql.cursors.DictCursor


def _connect_to_db(
    host=HOST,
    port=3306,
    db_user = DB_USER,
    password=PASSWORD,
    db=DB,
    charset=CHARSET,
    cursorclass=CURSORCLASS):

    try:
        conn = pymysql.connect(host=host, user=db_user, password=password, db=db, charset=charset, cursorclass=cursorclass)
        return conn
    except Exception as e:
        print('errror: ', e)




def insertar_pacientes(nombre,apellidop,apellidom,sexo,peso,estatura,edad,telefono,alergias,id_sangre):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""INSERT INTO pacientes(nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,alergiasPaciente,idTipo_Sangre_F) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nombre,apellidop,apellidom,sexo,peso,estatura,edad,telefono,alergias,id_sangre))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM pacientes"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

#hola = insertar_pacientes("Pedro","Torres","Padilla","Masculino","90.5","1.70","18","1234567890","Ninguna","2")
#print(hola)
#print("**************************************")
#sangresita = get_pacientes()
#print(sangresita)