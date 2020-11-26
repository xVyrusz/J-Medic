import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import modulos.db_Consultas as consultas


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Eliminar Consultas.ui", self)
        self.setWindowTitle("J-Medic: Eliminar Consulta")
        self.boton_Buscar.clicked.connect(self.validar_datos_idc)
        self.boton_Guardar.clicked.connect(self.validar_datos_idc_2)
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
            result = consultas.buscar_consulta_id(int(self.input_idc.text()))
            print(result)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            # self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result

            try:
                self.tabla_consultas.setItem(
                    0, 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_consultas.setItem(0, 1, QTableWidgetItem(ayuda[1]))
                self.tabla_consultas.setItem(
                    0, 2, QTableWidgetItem(str(ayuda[2])))
                self.tabla_consultas.setItem(0, 3, QTableWidgetItem(ayuda[3]))
                self.tabla_consultas.setItem(0, 4, QTableWidgetItem(ayuda[4]))
                self.tabla_consultas.setItem(
                    0, 5, QTableWidgetItem(str(ayuda[5])))
                self.tabla_consultas.setItem(
                    0, 6, QTableWidgetItem(str(ayuda[6])))
                self.tabla_consultas.setItem(
                    0, 7, QTableWidgetItem(str(ayuda[7])))
                self.tabla_consultas.setItem(0, 8, QTableWidgetItem(ayuda[8]))
                self.tabla_consultas.setItem(0, 9, QTableWidgetItem(ayuda[9]))
                # self.input_MedicoId.setText(str(ayuda[1]))
                # self.input_PacienteId.setText(str(ayuda[2]))
                # self.motivo_consulta.setText(str(ayuda[3]))
                # self.input_fecha.setText(str(ayuda[4]))
                # self.input_Pruebas.setText(str(ayuda[5]))
                # self.input_Diagnostico.setText(str(ayuda[6]))
                # self.input_Tratamiento.setText(str(ayuda[7]))
            except:
                QMessageBox.warning(
                    self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

            result2 = consultas.buscar_consulta_id_2(
                int(self.input_idc.text()))
            print(result2)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            # self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda2 = result2

            try:
                self.input_MedicoId.setText(str(ayuda2[1]))
                self.input_PacienteId.setText(str(ayuda2[2]))
                self.motivo_consulta.setText(str(ayuda2[3]))
                self.input_fecha.setText(str(ayuda2[4]))
                self.input_Pruebas.setText(str(ayuda2[5]))
                self.input_Diagnostico.setText(str(ayuda2[6]))
                self.input_Tratamiento.setText(str(ayuda2[7]))
            except:
                QMessageBox.warning(
                    self, "Error", "No se ha encontrado nada", QMessageBox.Discard)

            #QMessageBox.information(self, "Datos eliminados", "Se eliminaron los datos correctamente", QMessageBox.Discard)
            # self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_datos_idc_2(self):
        if self.validar_id_consulta():
            result = consultas.eliminar_consulta(int(self.input_idc.text()))
            print(result)
            result2 = consultas.eliminar_datos_consulta(
                int(self.input_idc.text()))
            print(result2)
            QMessageBox.information(
                self, "Datos eliminados", "Se eliminaron los datos correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)
    def switch(self):
        self.switch_window.emit()
