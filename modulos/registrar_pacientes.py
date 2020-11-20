import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import modulos.db_Pacientes as pacientes


class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/registro_pacientes.ui", self)
        self.setWindowTitle("J-Medic: Menu 1")
        self.boton_Guardar.clicked.connect(self.validar_datos)
        self.actionRegresar.setShortcut("Ctrl+R")
        self.actionRegresar.triggered.connect(self.switch)
        self.validar()

    def validar(self):
        self.input_Nombre.textChanged.connect(self.validar_nombre)
        self.input_ApellidoP.textChanged.connect(self.validar_apellidoP)
        self.input_ApellidoM.textChanged.connect(self.validar_apellidoM)
        self.input_Telefono.textChanged.connect(self.validar_telefono)
        self.input_Alergias.textChanged.connect(self.validar_alergia)
        pass

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

    def validar_sexo(self):
        sexo = self.combo_sexo.currentText()
        self.input_sexo.setText(str(sexo))
        sexo = self.input_sexo.text()
        if sexo == "":
            self.input_sexo.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_sexo.setStyleSheet("border: 2px solid green;")
            return True

    def validar_peso(self):
        pesok = self.comboBox.currentText()
        pesog = self.comboBox_2.currentText()
        cont = 0
        if pesog == "":
            cont += 1

        if pesok == "":
            cont += 1

        self.input_Peso.setText(str(pesok)+(pesog))
        if cont > 0:
            self.input_Peso.setText("")

        peso = self.input_Peso.text()
        if peso == "":
            self.input_Peso.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_Peso.setStyleSheet("border: 2px solid green;")
            return True

    def validar_estatura(self):
        estaturam = self.comboBox_3.currentText()
        estaturacm = self.comboBox_4.currentText()
        cont = 0
        if estaturacm == "":
            cont += 1

        if estaturam == "":
            cont += 1

        self.input_estatura.setText(str(estaturam)+(estaturacm))
        if cont > 0:
            self.input_estatura.setText("")

        estatura = self.input_estatura.text()
        if estatura == "":
            self.input_estatura.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_estatura.setStyleSheet("border: 2px solid green;")
            return True

    def validar_anios(self):
        anios = self.comboBox_5.currentText()
        self.input_anios.setText(str(anios))
        anios = self.input_anios.text()
        if anios == "":
            self.input_anios.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_anios.setStyleSheet("border: 2px solid green;")
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

    def validar_sangre(self):
        sangre = self.input_TipoS.currentText()
        self.input_sangre.setText(str(sangre))
        sangre = self.input_sangre.text()
        if sangre == "":
            self.input_sangre.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_sangre.setStyleSheet("border: 2px solid green;")
            return True

    def validar_alergia(self):
        alergias = self.input_Alergias.text()
        validar = re.match(
            "^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}$", alergias, re.I)
        if alergias == "":
            self.input_Alergias.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.input_Alergias.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.input_Alergias.setStyleSheet("border: 2px solid green;")
            return True

    def validar_datos(self):
        if self.validar_nombre() and self.validar_sexo() and self.validar_apellidoP() and self.validar_peso() and self.validar_apellidoM() and self.validar_estatura() and self.validar_telefono() and self.validar_anios() and self.validar_alergia() and self.validar_sangre():
            sangre = 0
            if self.input_sangre.text() == 'A+':
                sangre = 1
            elif self.input_sangre.text() == 'A-':
                sangre = 2
            elif self.input_sangre.text() == 'AB+':
                sangre = 3
            elif self.input_sangre.text() == 'AB-':
                sangre = 4
            elif self.input_sangre.text() == 'B+':
                sangre = 5
            elif self.input_sangre.text() == 'B-':
                sangre = 6
            elif self.input_sangre.text() == 'O+':
                sangre = 7
            elif self.input_sangre.text() == 'O-':
                sangre = 8
            else:
                sangre = 1

            pacientes.insertar_pacientes(self.input_Nombre.text(), self.input_ApellidoP.text(), self.input_ApellidoM.text(), self.input_sexo.text(),self.input_Peso.text(), self.input_estatura.text(), self.input_anios.text(), self.input_Telefono.text(), self.input_Alergias.text(), sangre)
            QMessageBox.information(
                self, "Datos guardados", "Su informacion se ha guardado correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(
                self, "Error", "Ingresa los datos correctamente", QMessageBox.Discard)

    def switch(self):
        self.switch_window.emit()
