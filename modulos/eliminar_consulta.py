import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Eliminar Consultas.ui", self)
        self.setWindowTitle("J-Medic: Eliminar Consulta")
        self.boton_Buscar.clicked.connect(self.validar_datos_idc)
        self.boton_Guardar.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idc.textChanged.connect(self.validar_id_consulta)
        pass

    def validar_id_consulta(self):
        id_consulta = self.input_idc.text()
        validar = re.match("^\d{1,}$", id_consulta, re.I)
        if id_consulta == "":
            self.input_idc.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_idc.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_idc.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_idc(self):
        if self.validar_id_consulta():
            QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
