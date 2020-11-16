from  import _connect_to_db


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

def eliminar(id):
    pass

sangresita = get_blood()
print(sangresita)