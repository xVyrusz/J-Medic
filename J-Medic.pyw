import sys, os, re, ctypes
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic

class Ventana(QMainWindow):

    def __init__(self):
        #iniciar el objeto
        QMainWindow.__init__(self)
        self.vista_inicioSesion()
        self.centrar_ventana()
        self.tamaño_ventana()
        self.boton_iniciarsesion.clicked.connect(self.validar_datos)
        
    def tamaño_ventana(self):
        #Fijas el tamaño mínimo
        self.setMinimumSize(500,500)
        #Fijas el tamaño máximo
        self.setMaximumSize(800,600)

    def centrar_ventana(self):
        #Mover la Ventana y centrarla en el escritorio
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)
        left = (resolucion_ancho / 2) - (self.frameSize().width() / 2)
        top = (resolucion_alto / 2) - (self.frameSize().width() / 2)
        self.move(left, top)

    def vista_inicioSesion(self):
        #Cargar la interfaz
        uic.loadUi("interfaces/iniciar_sesion.ui", self)
        #Fijar el titulo de la ventana
        self.setWindowTitle("J-Medic: Inicio de Sesion")

    def validar_datos(self):
        #Cargar la interfaz
        uic.loadUi("interfaces/Buscar medico.ui", self)
        #Fijar el titulo de la ventana
        self.setWindowTitle("J-Medic: Buscar medico")

    pass





#iniciar aplicacion
app = QApplication(sys.argv)
#Crear Objeto
_ventana = Ventana()
#Mostrar ventana
_ventana.show()
#Ejecuar Aplicacion
app.exec_()