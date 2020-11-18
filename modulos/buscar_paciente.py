import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/buscar_pacientes.ui", self)
        self.setWindowTitle("J-Medic: Buscar Paciente")
        self.boton_BuscarId.clicked.connect(self.validar_datos_id)
        self.boton_BuscarNombre.clicked.connect(self.validar_datos_nombre)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_BuscarId.textChanged.connect(self.validar_id)
        self.input_BuscarNombre.textChanged.connect(self.validar_nombre)
        pass

    def validar_id(self):
        aidi = self.input_BuscarId.text()
        validar = re.match("^\d{1,}$", aidi, re.I)
        if aidi == "":
            self.input_BuscarId.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_BuscarId.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_BuscarId.setStyleSheet("border: 2px solid green;")
            return True

    def validar_nombre(self):
        nombre = self.input_BuscarNombre.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_BuscarNombre.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_BuscarNombre.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_BuscarNombre.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_id(self):
        if self.validar_id():
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_datos_nombre(self):
        if self.validar_nombre():
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
