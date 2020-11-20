import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget
import modulos.db_Medicos as medicos

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
            result= medicos.buscar_medicos_id(int(self.input_id_medico.text()))
            print (result)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            #self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result
            try:
                self.tabla_buscar_medico.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_buscar_medico.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.tabla_buscar_medico.setItem(0 , 2, QTableWidgetItem(ayuda[2]))
                self.tabla_buscar_medico.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tabla_buscar_medico.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tabla_buscar_medico.setItem(0 , 5, QTableWidgetItem(ayuda[5]))
                self.tabla_buscar_medico.setItem(0 , 6, QTableWidgetItem(ayuda[6]))
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
