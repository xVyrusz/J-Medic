import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget
import modulos.db_Pacientes as pacientes

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
            result= pacientes.buscar_pacientes_id(int(self.input_BuscarId.text()))
            result2= pacientes.buscar_pacientes_id_consulta(int(self.input_BuscarId.text()))

            print (result2)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            #self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result
            ayuda2 = result2
            try:
                self.tabla_Pacientes.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_Pacientes.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.tabla_Pacientes.setItem(0 , 2, QTableWidgetItem(ayuda[2]))
                self.tabla_Pacientes.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tabla_Pacientes.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tabla_Pacientes.setItem(0 , 5, QTableWidgetItem(str(ayuda[5])))
                self.tabla_Pacientes.setItem(0 , 6, QTableWidgetItem(str(ayuda[6])))
                self.tabla_Pacientes.setItem(0 , 7, QTableWidgetItem(str(ayuda[7])))
                self.tabla_Pacientes.setItem(0 , 8, QTableWidgetItem(ayuda[8]))
                self.tabla_Pacientes.setItem(0 , 9, QTableWidgetItem(ayuda[9]))
                self.tabla_Pacientes.setItem(0 , 10, QTableWidgetItem(ayuda[10]))

                contador = 0
                for elements in ayuda2:
                    self.tabla_Consultas.setItem(contador , 0, QTableWidgetItem(str(ayuda2[contador][0])))
                    self.tabla_Consultas.setItem(contador , 1, QTableWidgetItem(str(ayuda2[contador][1])))
                    self.tabla_Consultas.setItem(contador , 2, QTableWidgetItem(ayuda2[contador][2]))
                    self.tabla_Consultas.setItem(contador , 3, QTableWidgetItem(ayuda2[contador][3]))
                    self.tabla_Consultas.setItem(contador , 4, QTableWidgetItem(ayuda2[contador][4]))
                    self.tabla_Consultas.setItem(contador , 5, QTableWidgetItem(ayuda2[contador][5]))
                    self.tabla_Consultas.setItem(contador , 6, QTableWidgetItem(str(ayuda2[contador][6])))
                    self.tabla_Consultas.setItem(contador , 7, QTableWidgetItem(ayuda2[contador][7]))
                    self.tabla_Consultas.setItem(contador , 8, QTableWidgetItem(ayuda2[contador][8]))
                    self.tabla_Consultas.setItem(contador , 9, QTableWidgetItem(ayuda2[contador][9]))
                    self.tabla_Consultas.setItem(contador , 10, QTableWidgetItem(ayuda2[contador][10]))
                    contador+=1
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

            #self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_datos_nombre(self):
        if self.validar_nombre():
            result= pacientes.buscar_pacientes_nombre(self.input_BuscarNombre.text())
            result2= pacientes.buscar_pacientes_nombre_consulta(self.input_BuscarNombre.text())

            print (result2)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            #self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result
            ayuda2 = result2
            
            try:
                self.tabla_Pacientes.setItem(0 , 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_Pacientes.setItem(0 , 1, QTableWidgetItem(ayuda[1]))
                self.tabla_Pacientes.setItem(0 , 2, QTableWidgetItem(ayuda[2]))
                self.tabla_Pacientes.setItem(0 , 3, QTableWidgetItem(ayuda[3]))
                self.tabla_Pacientes.setItem(0 , 4, QTableWidgetItem(ayuda[4]))
                self.tabla_Pacientes.setItem(0 , 5, QTableWidgetItem(str(ayuda[5])))
                self.tabla_Pacientes.setItem(0 , 6, QTableWidgetItem(str(ayuda[6])))
                self.tabla_Pacientes.setItem(0 , 7, QTableWidgetItem(str(ayuda[7])))
                self.tabla_Pacientes.setItem(0 , 8, QTableWidgetItem(ayuda[8]))
                self.tabla_Pacientes.setItem(0 , 9, QTableWidgetItem(ayuda[9]))
                self.tabla_Pacientes.setItem(0 , 10, QTableWidgetItem(ayuda[10]))

                contador = 0
                for elements in ayuda2:
                    self.tabla_Consultas.setItem(contador , 0, QTableWidgetItem(str(ayuda2[contador][0])))
                    self.tabla_Consultas.setItem(contador , 1, QTableWidgetItem(str(ayuda2[contador][1])))
                    self.tabla_Consultas.setItem(contador , 2, QTableWidgetItem(ayuda2[contador][2]))
                    self.tabla_Consultas.setItem(contador , 3, QTableWidgetItem(ayuda2[contador][3]))
                    self.tabla_Consultas.setItem(contador , 4, QTableWidgetItem(ayuda2[contador][4]))
                    self.tabla_Consultas.setItem(contador , 5, QTableWidgetItem(ayuda2[contador][5]))
                    self.tabla_Consultas.setItem(contador , 6, QTableWidgetItem(str(ayuda2[contador][6])))
                    self.tabla_Consultas.setItem(contador , 7, QTableWidgetItem(ayuda2[contador][7]))
                    self.tabla_Consultas.setItem(contador , 8, QTableWidgetItem(ayuda2[contador][8]))
                    self.tabla_Consultas.setItem(contador , 9, QTableWidgetItem(ayuda2[contador][9]))
                    self.tabla_Consultas.setItem(contador , 10, QTableWidgetItem(ayuda2[contador][10]))
                    contador+=1
            except:
                QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

            
            #self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
