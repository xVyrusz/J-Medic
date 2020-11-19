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




def get_pacientes():
    result = {}
    connection = _connect_to_db()
    try:
        with connection.cursor() as cursor:
            row_count = 0
            e='none'
            sql = f"""SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre """
            cursor.execute(sql)
            result = cursor.fetchall()
            print("Total rows are:  ", len(result))
            print("Printing each row")
            for row in result:
                print("Id: ", setRowCount[0])
                print("Name: ", row[1])
                print("Email: ", row[2])
                print("Salary: ", row[3])
                print("Id: ", row[4])
                print("Name: ", row[5])
                print("Email: ", row[6])
                print("Salary: ", row[7])
                print("Id: ", row[8])
                print("Name: ", row[9])
                print("Email: ", row[10])
                print("\n")


            cursor.close()
    except Exception as e:
        print(e)
        e.ex.args[0]
    finally:
        connection.close()
        return result

#hola = insertar_pacientes("Pedro","Torres","Padilla","Masculino","90.5","1.70","18","1234567890","Ninguna","2")
#print(hola)
#print("**************************************")
sangresita = get_pacientes()
#print(sangresita)

