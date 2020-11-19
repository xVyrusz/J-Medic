import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Registrar_medicos.ui", self)
        self.setWindowTitle("J-Medic: Registrar Medicos")
        self.Boton_Guardar.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_Nombre.textChanged.connect(self.validar_nombre)
        self.input_ApellidoP.textChanged.connect(self.validar_apellidoP)
        self.input_ApellidoM.textChanged.connect(self.validar_apellidoM)
        self.input_Cedula.textChanged.connect(self.validar_cedula)
        self.input_Telefono.textChanged.connect(self.validar_telefono)
        self.input_turno.textChanged.connect(self.seleccionar_turno)
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

    def seleccionar_turno(self):
        turno = self.input_Turno_2.currentText()
        self.input_turno.setText(str(turno))
        self.validar_turno()


    def validar_turno(self):
        turno = self.input_turno.text()
        if turno == "":
            self.input_turno.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_turno.setStyleSheet("border: 2px solid green;")
            self.validar_datos()
            return True

    def validar_datos(self):
        if self.validar_nombre and self.validar_apellidoP and self.validar_apellidoM and self.validar_cedula and self.validar_telefono and self.validar_turno == False:
            return False
        else:
            self.switch()
            return True


    def switch(self):
        self.switch_window.emit()
