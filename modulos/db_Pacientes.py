import modulos.db_conexion as conexion


def insertar_pacientes(nombre, apellidop, apellidom, sexo, peso, estatura, edad, telefono, alergias, sangre):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        sql = "INSERT INTO pacientes (nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,alergiasPaciente,idTipo_Sangre_F) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (nombre, apellidop, apellidom, sexo, peso,
               estatura, edad, telefono, alergias, sangre)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def editar_pacientes(nombre, apellidop, apellidom, sexo, peso, estatura, edad, telefono, alergias, sangre, idn):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        #sql = """UPDATE pacientes SET idTipo_Sangre_F = %s WHERE idPaciente = %s"""
        sql = """UPDATE pacientes SET nombrePaciente = %s, apellidoPPaciente = %s,apellidoMPaciente =%s,sexoPaciente = %s, pesoPaciente =%s, estaturaPaciente = %s, edadPaciente = %s, telefonoPaciente = %s, alergiasPaciente = %s, idTipo_Sangre_F = %s WHERE idPaciente = %s """
        val = (nombre, apellidop, apellidom, sexo, peso,
               estatura, edad, telefono, alergias, sangre, idn)
        #val = (sangre,idn)
        mycursor.execute(sql, val)
        mydb.commit()
        result = 1
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_pacientes_id(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente 
                FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre
                WHERE pacientes.idPaciente= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_pacientes_id_consulta(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """SELECT pacientes.idPaciente , datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F where  pacientes.idPaciente= {}""".format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_pacientes_nombre(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """
            SELECT pacientes.idPaciente,nombrePaciente,apellidoPPaciente,apellidoMPaciente,sexoPaciente,pesoPaciente,estaturaPaciente,edadPaciente,telefonoPaciente,tipo_sangre.nombreSangre,pacientes.alergiasPaciente 
            FROM pacientes inner join tipo_sangre on pacientes.idTipo_sangre_F=tipo_sangre.idTipo_sangre
            WHERE  pacientes.nombrePaciente= '{}' """.format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchone()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()


def buscar_pacientes_nombre_consulta(id):
    try:
        mydb = conexion.conexion()
        mycursor = mydb.cursor()
        if id:
            consult = """SELECT pacientes.idPaciente , datos_de_consulta.idConsulta,medicos.nombreMedico,medicos.apellidoPMedico,pacientes.nombrePaciente,pacientes.apellidoPPaciente,datos_de_consulta.fechaVisita,
            motivos_de_consulta.nombreMotivo,consulta.pruebasRealizadas,consulta.diagnostico,consulta.tratamiento FROM datos_de_consulta inner join medicos on medicos.idMedicos=datos_de_consulta.idMedicos_F
            inner join pacientes on datos_de_consulta.idPaciente_F=pacientes.idPaciente
            inner join motivos_de_consulta on motivos_de_consulta.idMotivos_de_Consulta=datos_de_consulta.idMotivo_F
            inner join consulta on datos_de_consulta.idConsulta=consulta.idConsulta_F where pacientes.nombrePaciente ='{}' """.format(id)
        else:
            raise Exception('Id is needed')
        mycursor.execute(consult)
        result = mycursor.fetchall()
        return result
    except:
        print('Something wrong happend 😡😡😡😠😡😡😡')
    finally:
        mydb.close()
        mycursor.close()
