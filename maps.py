from PyQt5.QtWidgets import QMainWindow, QApplication
from maps_gui import Ui_MainWindow

import sys


class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.gui = GUI()

    def run(self):
        self.gui.show()

        sys.exit(self.app.exec_())


if __name__ == '__main__':
    main = Main()
    main.run()
