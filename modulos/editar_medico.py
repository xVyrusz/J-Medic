import re
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
import modulos.db_Medicos as medicos


class WindowTree(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/editar_medicos.ui", self)
        self.setWindowTitle("J-Medic: Editar Medico")
        self.boton_buscar.clicked.connect(self.validar_datos_id)
        self.boton_editar.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_Nombre.textChanged.connect(self.validar_nombre)
        self.input_ApellidoP.textChanged.connect(self.validar_apellidoP)
        self.input_ApellidoM.textChanged.connect(self.validar_apellidoM)
        self.input_Telefono.textChanged.connect(self.validar_telefono)
        self.input_Cedula.textChanged.connect(self.validar_cedula)
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
            result = medicos.buscar_medicos_id(
                int(self.input_id_medico.text()))
            print(result)
            #rowPosition = self.tabla_buscar_medico.rowCount()
            # self.tabla_buscar_medico.insertRow(rowPosition)
            ayuda = result
            try:
                self.tabla_buscar_medico.setItem(
                    0, 0, QTableWidgetItem(str(ayuda[0])))
                self.tabla_buscar_medico.setItem(
                    0, 1, QTableWidgetItem(ayuda[1]))
                self.tabla_buscar_medico.setItem(
                    0, 2, QTableWidgetItem(ayuda[2]))
                self.tabla_buscar_medico.setItem(
                    0, 3, QTableWidgetItem(ayuda[3]))
                self.tabla_buscar_medico.setItem(
                    0, 4, QTableWidgetItem(ayuda[4]))
                self.tabla_buscar_medico.setItem(
                    0, 5, QTableWidgetItem(ayuda[5]))
                self.tabla_buscar_medico.setItem(
                    0, 6, QTableWidgetItem(ayuda[6]))
                self.input_Nombre.setText(str(ayuda[1]))
                self.input_ApellidoP.setText(str(ayuda[2]))
                self.input_ApellidoM.setText(str(ayuda[3]))
                self.input_Cedula.setText(str(ayuda[4]))
                self.input_Telefono.setText(str(ayuda[5]))
                self.input_turno.setText(str(ayuda[6]))
            except:
                QMessageBox.warning(
                    self, "Error", "No se ha encontrado nada", QMessageBox.Discard)
                
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)
    def validar_nombre(self):
        nombre = self.input_Nombre.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", nombre, re.I)
        if nombre == "":
            self.input_Nombre.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Nombre.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Nombre.setStyleSheet("border: 2px solid green;")
            return True

    def validar_apellidoP(self):
        apellido = self.input_ApellidoP.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.input_ApellidoP.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ApellidoP.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ApellidoP.setStyleSheet("border: 2px solid green;")
            return True

    def validar_apellidoM(self):
        apellido = self.input_ApellidoM.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", apellido, re.I)
        if apellido == "":
            self.input_ApellidoM.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_ApellidoM.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_ApellidoM.setStyleSheet("border: 2px solid green;")
            return True

    def validar_cedula(self):
        cedula = self.input_Cedula.text()
        validar = re.match("^\d{1,}$", cedula, re.I)
        if cedula == "":
            self.input_Cedula.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Cedula.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Cedula.setStyleSheet("border: 2px solid green;")
            return True

    def validar_telefono(self):
        telefono = self.input_Telefono.text()
        validar = re.match("^\d{10}$", telefono, re.I)
        if telefono == "":
            self.input_Telefono.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Telefono.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Telefono.setStyleSheet("border: 2px solid green;")
            return True

    def validar_turno(self):
        turno = self.input_Turno_2.currentText()
        self.input_turno.setText(str(turno))
        turno = self.input_turno.text()
        if turno == "":
            self.input_turno.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_turno.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_nombre() and self.validar_cedula() and self.validar_apellidoP() and self.validar_turno() and self.validar_apellidoM() and self.validar_telefono():
            sangre = ''
            if self.input_turno.text() == 'Matutino':
                sangre = '1'
            elif self.input_turno.text() == 'Vespertino':
                sangre = '2'
            else:
                sangre = '1'
            #result = medicos.editar_medico(self.input_Nombre.text(),self.input_id_medico.text())
            result = medicos.editar_medico(self.input_Nombre.text(), self.input_ApellidoP.text(), self.input_ApellidoM.text(
            ), self.input_Cedula.text(), self.input_Telefono.text(), sangre, self.input_id_medico.text())
            print(result)

            QMessageBox.information(
                self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
