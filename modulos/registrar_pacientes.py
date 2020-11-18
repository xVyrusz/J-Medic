import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets
import db_operations.conexion as _connect_to_db
import db_operations.Pacientes as insertar_pacientes

class WindowTwo(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/registro_pacientes.ui", self)
        self.setWindowTitle("J-Medic: Menu 1")
        self.boton_Guardar.clicked.connect(self.seleccionar_sexo)
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

    def seleccionar_sexo(self):
        sexo = self.combo_sexo.currentText()
        self.input_sexo.setText(str(sexo))
        self.validar_sexo()


    def validar_sexo(self):
        sexo = self.input_sexo.text()
        if sexo == "":
            self.input_sexo.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_sexo.setStyleSheet("border: 2px solid green;")
            self.seleccionar_peso()
            return True

    def seleccionar_peso(self):
        pesok = self.comboBox.currentText()
        pesog = self.comboBox_2.currentText()
        self.input_Peso.setText(str(pesok)+(pesog))
        self.validar_peso()

    def validar_peso(self):
        peso = self.input_Peso.text()
        if peso == "":
            self.input_Peso.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_Peso.setStyleSheet("border: 2px solid green;")
            self.seleccionar_estatura()
            return True

    def seleccionar_estatura(self):
        estaturam = self.comboBox_3.currentText()
        estaturacm = self.comboBox_4.currentText()
        self.input_estatura.setText(str(estaturam)+(estaturacm))
        self.validar_estatura()

    def validar_estatura(self):
        estatura = self.input_estatura.text()
        if estatura == "":
            self.input_estatura.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_estatura.setStyleSheet("border: 2px solid green;")
            self.seleccionar_anios()
            return True

    def seleccionar_anios(self):
        anios = self.comboBox_5.currentText()
        self.input_anios.setText(str(anios))
        self.validar_anios()

    def validar_anios(self):
        anios = self.input_anios.text()
        if anios == "":
            self.input_anios.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_anios.setStyleSheet("border: 2px solid green;")
            self.seleccionar_sangre()
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

    def seleccionar_sangre(self):
        sangre = self.input_TipoS.currentText()
        self.input_sangre.setText(str(sangre))
        self.validar_sangre()

    def validar_sangre(self):
        sangre = self.input_sangre.text()
        if sangre == "":
            self.input_sangre.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_sangre.setStyleSheet("border: 2px solid green;")
            self.validar_datos()
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
        if self.validar_nombre and self.validar_apellidoP and self.validar_apellidoM and self.validar_sexo and self.validar_telefono and self.validar_peso and self.validar_estatura and self.validar_anios and self.validar_sangre and self.validar_alergia == False:
            return False
        else:
            self.insertar_pacientes()
            self.switch()
            return True

    def switch(self):
        self.switch_window.emit()
