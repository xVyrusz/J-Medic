import sys, os, re, ctypes
from PyQt5 import uic, QtCore, QtWidgets
import modulos.iniciosesion as iniciosesion
import modulos.menu as menu

class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = iniciosesion.Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = menu.MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()