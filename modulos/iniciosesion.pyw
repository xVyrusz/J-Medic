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

    def login(self):
        self.switch_window.emit()
