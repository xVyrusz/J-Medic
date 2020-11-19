import sys
import os
import re
import ctypes
from PyQt5 import uic, QtCore, QtWidgets


class Login(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/iniciar_sesion.ui", self)
        self.setWindowTitle("J-Medic: Inicio de Sesion")
        self.boton_iniciar.clicked.connect(self.login)
        self.validar()

    def validar(self):
        self.input_user.textChanged.connect(self.validar_usuario)
        pass

    def encriptacion(self):
        contra = self.input_Contra.text()
        if bcrypt.checkpw(contra.encode(), hashed.encode()):
            return True
        else:
            return False

    def validar_usuario(self):
        user = self.input_user.text()
        if user == "":
            self.input_user.setStyleSheet("border: 2px solid yellow;")
            return False
        else:
            self.input_user.setStyleSheet("border: 2px solid green;")
            return True


    def validar_datos(self):
        if self.validar_usuario() and self.encriptacion():
            QMessageBox.information(self, "Exito", "Ingreso correctamente", QMessageBox.Discard)
            self.switch()
        else:
            QMessageBox.warning(self, "Error", "El usuario o la contraseña estan incorrectos", QMessageBox.Discard)

    def login(self):
        self.switch_window.emit()
