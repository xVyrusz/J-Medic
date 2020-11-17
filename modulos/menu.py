import sys, os, re, ctypes
from PyQt5 import uic, QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()
    switch_window7 = QtCore.pyqtSignal()
    switch_window8 = QtCore.pyqtSignal()
    switch_window9 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("interfaces/menu.ui", self)
        self.setWindowTitle("J-Medic: Menu 1")
        self.boton_AgregarMedico.clicked.connect(self.switch)
        self.boton_AgregarPaciente.clicked.connect(self.switch2)
        self.boton_AgregarConsulta.clicked.connect(self.switch3)
        self.boton_AgregarCita.clicked.connect(self.switch4)
        self.boton_BuscarMedico.clicked.connect(self.switch5)
        self.boton_BuscarPaciente.clicked.connect(self.switch6)
        self.boton_BuscarConsulta.clicked.connect(self.switch7)
        self.boton_BuscarCita.clicked.connect(self.switch8)
        self.boton_MasOpciones.clicked.connect(self.switch9)




    def switch(self):
        self.switch_window.emit()

    def switch2(self):
        self.switch_window2.emit()
    
    def switch3(self):
        self.switch_window3.emit()

    def switch4(self):
        self.switch_window4.emit()
    
    def switch5(self):
        self.switch_window5.emit()

    def switch6(self):
        self.switch_window6.emit()

    def switch7(self):
        self.switch_window7.emit()

    def switch8(self):
        self.switch_window8.emit()
    
    def switch9(self):
        self.switch_window9.emit()