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


def get_blood():
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            #Read everything of tipo_sangre
            sql = f"""SELECT * FROM pacientes"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def traer_medicos():
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            #Read everything of <UNA TABLA>
            sql = f"""SELECT * FROM tipo_sangre"""
            cursor.execute(sql)
            result = cursor.fetchall()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result
#sangre es el parametro
def insertar_sangre(sangre):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""INSERT INTO tipo_sangre(nombreSangre) VALUES(%s)"""
            cursor.execute(sql, (sangre))
        connection.commit()
        with connection.cursor() as cursor:
            sql = f"""SELECT * FROM tipo_sangre"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

def insertar_pacientes(paciente):
    result = {}
    connection = _connect_to_db()

    try:
        with connection.cursor() as cursor:
            #Read everything of <UNA TABLA>
            sql = f"""INSERT INTO pacientes(nombrePaciente) VALUES(%s)"""
            cursor.execute(sql, (paciente))
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

hola = insertar_pacientes("Jesus")
print(hola)
print("**************************************")
#sangresita = get_blood()
#print(sangresita)