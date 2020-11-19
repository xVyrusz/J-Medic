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


if __name__ == '__main__':
    _connect_to_db()




#hola = insertar_pacientes("Jesus","carreon")
#print(hola)
#print("**************************************")
#sangresita = get_blood()
#print(sangresita)