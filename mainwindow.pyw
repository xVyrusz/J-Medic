import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

#Clase heredada de QMainWindow
class Ventana(QMainWindow):
    #Contructor
    def __init__(self):
        #iniciar el objeto
        QMainWindow.__init__(self)
        #Cargar la interfaz
        uic.loadUi("interfaces/registro_pacientes.ui", self)
        pass

    pass


#iniciar aplicacion
app = QApplication(sys.argv)
#Crear Objeto
_ventana = Ventana()
#Mostrar ventana
_ventana.show()
#Ejecuar Aplicacion
app.exec_()