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
        uic.loadUi("interfaces/buscar_consultas.ui", self)
        self.setWindowTitle("J-Medic: Buscar Consulta")
        self.boton_buscarid.clicked.connect(self.validar_datos_idc)
        self.boton_buscarmed.clicked.connect(self.validar_datos_nombre_medico)
        self.boton_buscarpac.clicked.connect(self.validar_datos_nombre_paciente)
        self.boton_buscarmotivo.clicked.connect(self.validar_datos_motivo)
        self.boton_buscarfecha.clicked.connect(self.validar_datos_fecha)
        self.boton_mostrartodo.clicked.connect(self.switch)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idc.textChanged.connect(self.validar_id_consulta)
        self.input_medico.textChanged.connect(self.validar_nombre_medico)
        self.input_paciente.textChanged.connect(self.validar_nombre_paciente)
        self.input_motivo.textChanged.connect(self.validar_motivo)
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

    def validar_nombre_medico(self):
        nombre = self.input_medico.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_medico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_medico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_medico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_nombre_medico(self):
        if self.validar_nombre_medico():
            QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def validar_nombre_paciente(self):
        nombre = self.input_paciente.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_paciente.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_paciente.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_paciente.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_nombre_paciente(self):
        if self.validar_nombre_paciente():
            QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def validar_motivo(self):
        motivos = self.motivo.currentText()
        self.input_motivo.setText(str(motivos))
        motivo = self.input_motivo.text()
        if motivo == "":
            self.input_motivo.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_motivo.setStyleSheet("border: 2px solid green;")
            return True


    def validar_datos_motivo(self):
        if self.validar_motivo():
            QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def seleccionar_fecha(self):
        anio = self.comboBox_4.currentText()
        mes = self.comboBox_3.currentText()
        dia = self.comboBox_2.currentText()
        self.input_fecha.setText(str(anio)+(mes)+(dia))
        fecha = self.input_fecha.text()
        if fecha == "":
            self.input_fecha.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_fecha.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_fecha(self):
        if self.validar_motivo():
            QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
