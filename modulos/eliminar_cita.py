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
        uic.loadUi("interfaces/eliminar_cita.ui", self)
        self.setWindowTitle("J-Medic: Eliminar Cita")
        self.boton_buscar.clicked.connect(self.validar_datos_id_cita)
        self.boton_eliminar.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idc.textChanged.connect(self.validar_id_cita)
        pass

    def validar_id_cita(self):
        id_cita = self.input_idc.text()
        validar = re.match("^\d{1,}$", id_cita, re.I)
        if id_cita == "":
            self.input_idc.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_idc.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_idc.setStyleSheet("border: 2px solid green;")
            return True


    def validar_datos_id_cita(self):
        if self.validar_id_cita():
            QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
