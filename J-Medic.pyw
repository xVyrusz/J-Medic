import sys, os, re, ctypes
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic, QtCore
import modulos.iniciosesion as iniciosesion

class Controller:

    def __init__(self):
        pass

    def iniciar_sesion(self):
        self.iniciar_sesion = iniciosesion.Ventana()
        self.iniciar_sesion.switch_window.connect(self.show_main)
        self.iniciar_sesion.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()



def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.iniciar_sesion()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()