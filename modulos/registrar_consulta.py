import sys
import os
import re
import ctypes
import datetime
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QTableWidget
import modulos.db_Consultas as consultas

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Nueva_consulta.ui", self)
        self.setWindowTitle("J-Medic: Registrar Consulta")
        self.guardar_consulta.clicked.connect(self.validar_datos_2)
        self.generar_idc.clicked.connect(self.validar_datos)
        self.generar_fecha.clicked.connect(self.seleccionar_fecha)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idm.textChanged.connect(self.validar_id_medico)
        self.input_idp.textChanged.connect(self.validar_id_paciente)
        self.input_idc.textChanged.connect(self.validar_id_consulta)
        pass

    def validar_id_medico(self):
        id_medico = self.input_idm.text()
        validar = re.match("^\d{1,}$", id_medico, re.I)
        if id_medico == "":
            self.input_idm.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_idm.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_idm.setStyleSheet("border: 2px solid green;")
            return True


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


    def seleccionar_motivo(self):
        motivos = self.motivo_consulta.currentText()
        self.input_motivo.setText(str(motivos))
        motivo = self.input_motivo.text()
        if motivo == "":
            self.input_motivo.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_motivo.setStyleSheet("border: 2px solid green;")
            return True


    def seleccionar_fecha(self):
        fecha_2 = datetime.date.today()
        fecha_3 = str(fecha_2)
        self.input_fecha.setText(str(fecha_3))
        fecha = self.input_fecha.text()
        if fecha == "":
            self.input_fecha.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_fecha.setStyleSheet("border: 2px solid green;")
            return True


    def validar_datos(self):
        cont = 0
        if self.validar_id_medico() and self.validar_id_paciente() and self.seleccionar_motivo() and self.seleccionar_fecha():
            motivo=0
            if self.input_motivo.text()=='Consulta General':
                motivo=1
            elif self.input_motivo.text()=='Curaciones':
                motivo=2
            elif self.input_motivo.text()=='Examenes':
                motivo=3
            else:
                motivo=1
            result =consultas.insertar_datos_de_consulta(self.input_idm.text(),self.input_idp.text(),self.input_fecha.text(),motivo)
            if result == 1:
                result2 =consultas.mostrar_datos_consulta()
                print(result2)

                ayuda = result2

                try:
                    if ayuda:
                        contador = 0
                        for elements in ayuda:
                            self.tabla_idc.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                            self.tabla_idc.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                            self.tabla_idc.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                            self.tabla_idc.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                            self.tabla_idc.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                            self.tabla_idc.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                            self.tabla_idc.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                            contador+=1
                    else:
                        QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
                except:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

                #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
                #self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


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

    def validar_pruebas(self):
        pruebas = self.pruebas_realizadas.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", pruebas, re.I)
        if pruebas == "":
            self.pruebas_realizadas.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.pruebas_realizadas.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.pruebas_realizadas.setStyleSheet("border: 2px solid green;")
            return True

    def validar_diagnostico(self):
        diag = self.diagnostico.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", diag, re.I)
        if diag == "":
            self.diagnostico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.diagnostico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.diagnostico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_tratamiento(self):
        trata = self.tratamiento.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", trata, re.I)
        if trata == "":
            self.tratamiento.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.tratamiento.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.tratamiento.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos_2(self):
        cont = 0
        if self.validar_id_consulta() and self.validar_pruebas() and self.validar_diagnostico() and self.validar_tratamiento():
            result =consultas.insertar_consulta(self.input_idc.text(),self.pruebas_realizadas.toPlainText(),self.diagnostico.toPlainText(),self.tratamiento.toPlainText())
            if result == 1:
                result3 =consultas.mostrar_datos_consulta_completa()
                print(result3)

                ayuda = result3

                try:
                    if ayuda:
                        contador = 0
                        for elements in ayuda:
                            self.tabla_consultas.setItem(contador , 0, QTableWidgetItem(str(ayuda[contador][0])))
                            self.tabla_consultas.setItem(contador , 1, QTableWidgetItem(ayuda[contador][1]))
                            self.tabla_consultas.setItem(contador , 2, QTableWidgetItem(str(ayuda[contador][2])))
                            self.tabla_consultas.setItem(contador , 3, QTableWidgetItem(ayuda[contador][3]))
                            self.tabla_consultas.setItem(contador , 4, QTableWidgetItem(ayuda[contador][4]))
                            self.tabla_consultas.setItem(contador , 5, QTableWidgetItem(str(ayuda[contador][5])))
                            self.tabla_consultas.setItem(contador , 6, QTableWidgetItem(str(ayuda[contador][6])))
                            self.tabla_consultas.setItem(contador , 7, QTableWidgetItem(str(ayuda[contador][7])))
                            self.tabla_consultas.setItem(contador , 8, QTableWidgetItem(str(ayuda[contador][8])))
                            self.tabla_consultas.setItem(contador , 9, QTableWidgetItem(str(ayuda[contador][9])))
                            contador+=1
                    else:
                        QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
                except:
                    QMessageBox.warning(self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
                    #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
                    #self.switch()
        else:
            QMessageBox.warning(self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)


    def switch(self):
        self.switch_window.emit()
