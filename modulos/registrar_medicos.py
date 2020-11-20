import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import modulos.db_Medicos as medicos

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Registrar_medicos.ui", self)
        self.setWindowTitle("J-Medic: Registrar Medicos")
        self.boton_guardar.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_Nombre.textChanged.connect(self.validar_nombre)
        self.input_ApellidoP.textChanged.connect(self.validar_apellidoP)
        self.input_ApellidoM.textChanged.connect(self.validar_apellidoM)
        self.input_Telefono.textChanged.connect(self.validar_telefono)
        self.input_Cedula.textChanged.connect(self.validar_cedula)
        self.input_user.textChanged.connect(self.validar_usuario)
        pass


    def validar_nombre(self):
        nombre = self.input_Nombre.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_Nombre.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Nombre.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Nombre.setStyleSheet("border: 2px solid green;")
            return True

    def validar_apellidoP(self):
        apellido = self.input_ApellidoP.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.input_ApellidoP.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ApellidoP.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ApellidoP.setStyleSheet("border: 2px solid green;")
            return True

    def validar_apellidoM(self):
        apellido = self.input_ApellidoM.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.input_ApellidoM.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ApellidoM.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ApellidoM.setStyleSheet("border: 2px solid green;")
            return True

    def validar_cedula(self):
        cedula = self.input_Cedula.text()
        validar = re.match("^\d{1,}$", cedula, re.I)
        if cedula == "":
            self.input_Cedula.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Cedula.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Cedula.setStyleSheet("border: 2px solid green;")
            return True

    def validar_telefono(self):
        telefono = self.input_Telefono.text()
        validar = re.match("^\d{10}$", telefono, re.I)
        if telefono == "":
            self.input_Telefono.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Telefono.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Telefono.setStyleSheet("border: 2px solid green;")
            return True

    def validar_turno(self):
        turno = self.input_Turno_2.currentText()
        self.input_turno.setText(str(turno))
        turno = self.input_turno.text()
        if turno == "":
            self.input_turno.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_turno.setStyleSheet("border: 2px solid green;")
            return True

    def validar_usuario(self):
        user = self.input_user.text()
        validar = re.match(
            "^[\w'\-,.][^!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", user, re.I)
        if user == "":
            self.input_user.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_user.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_user.setStyleSheet("border: 2px solid green;")
            return True

    def validar_password(self):
        contra = self.input_contra.text()
        if contra == "":
            self.input_contra.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_contra.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_nombre() and self.validar_cedula() and self.validar_apellidoP() and self.validar_turno() and self.validar_apellidoM() and self.validar_telefono() and self.validar_usuario() and self.validar_password():
            result =medicos.insertar_medicos(self.input_Nombre.text(),self.input_ApellidoP.text(),self.input_ApellidoM.text(),self.input_Cedula.text(),self.input_Telefono.text(),self.input_turno.text(),self.input_user.text(),self.input_contra.text())
            if result == 1:
                QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
                self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def switch(self):
        self.switch_window.emit()
