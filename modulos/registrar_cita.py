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
        uic.loadUi("interfaces/agendar_cita.ui", self)
        self.setWindowTitle("J-Medic: Registrar Cita")
        self.boton_agendar_cita.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idp.textChanged.connect(self.validar_id_paciente)
        self.input_fecha.textChanged.connect(self.validar_id_paciente)
        pass


    def validar_id_paciente(self):
        id_paciente = self.input_idp.text()
        validar = re.match("^\d{1,}$", id_paciente, re.I)
        if id_paciente == "":
            self.input_idp.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_idp.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_idp.setStyleSheet("border: 2px solid green;")
            return True

    def validar_fecha(self):
        anio = self.comboBox_4.currentText()
        mes = self.comboBox_3.currentText()
        dia = self.comboBox_2.currentText()
        hora = self.comboBox.currentText()
        minutos = self.comboBox_5.currentText()
        self.input_fecha.setText(str(anio)+(mes)+(dia)+(hora)+(minutos))
        fecha = self.input_fecha.text()
        if fecha == "":
            self.input_fecha.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_fecha.setStyleSheet("border: 2px solid green;")
            return True



    def validar_datos(self):
        if self.validar_id_paciente() and self.validar_fecha():
            QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
