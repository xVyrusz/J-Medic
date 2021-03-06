import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import modulos.db_Consultas as consultas


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/Editar_Consultas.ui", self)
        self.setWindowTitle("J-Medic: Editar Consulta")
        self.boton_Buscar.clicked.connect(self.validar_dato_id_consulta)
        self.input_Aceptar.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_MedicoId.textChanged.connect(self.validar_id_medico)
        self.input_PacienteId.textChanged.connect(self.validar_id_paciente)
        self.input_ConsultaId.textChanged.connect(self.validar_id_consulta)
        pass

    def validar_id_consulta(self):
        id_consulta = self.input_ConsultaId.text()
        validar = re.match("^\d{1,}$", id_consulta, re.I)
        if id_consulta == "":
            self.input_ConsultaId.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ConsultaId.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ConsultaId.setStyleSheet("border: 2px solid green;")
            return True

    def validar_dato_id_consulta(self):
        if self.validar_id_consulta():
            result = consultas.buscar_consulta_id(
                int(self.input_ConsultaId.text()))
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
                int(self.input_ConsultaId.text()))
            print(result2)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            # self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda2 = result2

            try:
                self.input_MedicoId.setText(str(ayuda2[1]))
                self.input_PacienteId.setText(str(ayuda2[2]))
                self.input_motivo.setText(str(ayuda2[3]))
                self.input_fecha.setText(str(ayuda2[4]))
                self.input_Pruebas.setText(str(ayuda2[5]))
                self.input_Diagnostico.setText(str(ayuda2[6]))
                self.input_Tratamiento.setText(str(ayuda2[7]))
            except:
                QMessageBox.warning(
                    self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
                #QMessageBox.information(self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def validar_id_medico(self):
        id_medico = self.input_MedicoId.text()
        validar = re.match("^\d{1,}$", id_medico, re.I)
        if id_medico == "":
            self.input_MedicoId.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_MedicoId.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_MedicoId.setStyleSheet("border: 2px solid green;")
            return True

    def validar_id_paciente(self):
        id_paciente = self.input_PacienteId.text()
        validar = re.match("^\d{1,}$", id_paciente, re.I)
        if id_paciente == "":
            self.input_PacienteId.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_PacienteId.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_PacienteId.setStyleSheet("border: 2px solid green;")
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
        anio = self.comboBox_4.currentText()
        mes = self.comboBox_3.currentText()
        dia = self.comboBox_2.currentText()
        cont = 0
        if anio == "":
            cont += 1

        if mes == "":
            cont += 1

        if dia == "":
            cont += 1

        self.input_fecha.setText(str(anio)+(mes)+(dia))
        if cont > 0:
            self.input_fecha.setText("")

        fecha = self.input_fecha.text()
        if fecha == "":
            self.input_fecha.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_fecha.setStyleSheet("border: 2px solid green;")
            return True

    def validar_pruebas(self):
        pruebas = self.input_Pruebas.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", pruebas, re.I)
        if pruebas == "":
            self.input_Pruebas.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Pruebas.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Pruebas.setStyleSheet("border: 2px solid green;")
            return True

    def validar_diagnostico(self):
        diag = self.input_Diagnostico.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", diag, re.I)
        if diag == "":
            self.input_Diagnostico.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Diagnostico.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Diagnostico.setStyleSheet("border: 2px solid green;")
            return True

    def validar_tratamiento(self):
        trata = self.input_Tratamiento.toPlainText()
        validar = re.match(
            "^[\w'\-,.][^_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", trata, re.I)
        if trata == "":
            self.input_Tratamiento.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Tratamiento.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Tratamiento.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        cont = 0
        if self.validar_id_medico() and self.validar_id_paciente() and self.seleccionar_motivo() and self.seleccionar_fecha() and self.validar_pruebas() and self.validar_diagnostico() and self.validar_tratamiento():
            sangre = ''
            if self.input_motivo.text() == 'Consulta General':
                sangre = '1'
            elif self.input_motivo.text() == 'Curaciones':
                sangre = '2'
            elif self.input_motivo.text() == 'Examenes':
                sangre = '3'
            else:
                sangre = '1'
            #result = medicos.editar_medico(self.input_Nombre.text(),self.input_id_medico.text())
            result = consultas.editar_datos_de_consulta(self.input_MedicoId.text(
            ), self.input_PacienteId.text(), self.input_fecha.text(), sangre, self.input_ConsultaId.text())
            print(result)
            result2 = consultas.editar_consulta(self.input_Pruebas.toPlainText(), self.input_Diagnostico.toPlainText(
            ), self.input_Tratamiento.toPlainText(), self.input_ConsultaId.text())
            QMessageBox.information(
                self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
