import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/registro_pacientes.ui", self)
        self.setWindowTitle("J-Medic: Menu 1")
        self.boton_Guardar.clicked.connect(self.validar_estatura)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_Nombre.textChanged.connect(self.validar_nombre)
        self.input_ApellidoP.textChanged.connect(self.validar_apellidoP)
        self.input_ApellidoM.textChanged.connect(self.validar_apellidoM)
        self.input_Telefono.textChanged.connect(self.validar_telefono)
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

    def validar_estatura(self):
        estatura = self.input_Estatura.value()
        
        self.Estatura.setText(str(estatura))

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

    def switch(self):
        self.switch_window.emit()
