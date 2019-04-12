from PyQt5.QtWidgets import QMainWindow
from big_API_maps.maps_gui import Ui_MainWindow


class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    gui = GUI()