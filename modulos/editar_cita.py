import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import modulos.db_cita as cita


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/editar_cita.ui", self)
        self.setWindowTitle("J-Medic: Editar Cita")
        self.boton_buscarc.clicked.connect(self.validar_datos_id_cita)
        self.boton_agendar.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_idp.textChanged.connect(self.validar_id_paciente)
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
            result = cita.buscar_cita_idcita(int(self.input_idc.text()))
            print(result)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            # self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result

            try:
                self.tabla_citas.setItem(0, 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_citas.setItem(0, 1, QTableWidgetItem(str(ayuda[1])))
                self.tabla_citas.setItem(0, 2, QTableWidgetItem(str(ayuda[2])))
                self.tabla_citas.setItem(0, 3, QTableWidgetItem(ayuda[3]))
                self.tabla_citas.setItem(0, 4, QTableWidgetItem(ayuda[4]))
                self.tabla_citas.setItem(0, 5, QTableWidgetItem(str(ayuda[5])))
                self.input_idp.setText(str(ayuda[1]))
                self.input_fecha.setText(str(ayuda[5]))
            except:
                QMessageBox.warning(
                    self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
            #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            # self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

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
        cont = 0
        if anio == "":
            cont += 1

        if mes == "":
            cont += 1

        if dia == "":
            cont += 1

        if hora == "":
            cont += 1

        if minutos == "":
            cont += 1

        self.input_fecha.setText(anio+'-'+mes+'-'+dia+hora+minutos)
        if cont > 0:
            self.input_fecha.setText("")

        fecha = self.input_fecha.text()
        if fecha == "":
            self.input_fecha.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_fecha.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_id_paciente() and self.validar_fecha():
            result = cita.editar_cita(self.input_idp.text(
            ), self.input_fecha.text(), self.input_idc.text())
            QMessageBox.information(
                self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
