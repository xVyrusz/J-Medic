import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import modulos.db_conexion as _connect_to_db
import modulos.db_Medicos as medicos
import pymysql.cursors
#import modulos.db_conexion as conexion

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Buscar medico.ui", self)
        self.setWindowTitle("J-Medic: Buscar Medico")
        self.boton_buscar.clicked.connect(self.validar_datos_id)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_id_medico.textChanged.connect(self.validar_id_medico)
        pass

    def validar_id_medico(self):
        id_medico = self.input_id_medico.text()
        validar = re.match("^\d{1,}$", id_medico, re.I)
        if id_medico == "":
            self.input_id_medico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_id_medico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_id_medico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_id(self):
        if self.validar_id_medico():
            medicos.buscar_medicos_id(self.input_id_medico.text())
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
                     self.table.setColumnCount (6)
                    self.table.setHorizontalHeaderLabels(['idMedicos','nombreMedico','apellidoPMedico','apellidoMMedico','Cedula','Telefono','idTurnos_F'])
                row =0
                sql ="SELECT *FROM medicos"
                query =QSqlQuery(sql)
                while query.next():
                    self.table.insertRow(row)
                    idMedicos=tabla2(str(query.value(0)))
                    nombreMedico=tabla_2(str(query.value(1)))
                    apellidoPMedico=tabla_2(str(query.value(2)))
                    apellidoMMedico=tabla2(str(query.value(3)))
                    Cedula=tabla_2(str(query.value(4)))
                    Telefono=tabla2(str(query.value(5)))
                    idTurnos_F=tabla_2(str(query.value(6)))
                    self.table.setItem(row, 0, idMedicos)
                    self.table.setItem(row, 1, nombreMedico)
                    self.table.setItem(row, 2, apellidoPMedico)
                    self.table.setItem(row, 3, apellidoMMedico)
                    self.table.setItem(row, 4, Cedula)
                    self.table.setItem(row, 5, Telefono)
                    self.table.setItem(row, 6, idTurnos_F)
                    row = row+1
            #self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()



