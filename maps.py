from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from maps_gui import Ui_MainWindow
from requester import geo

from tips import fetch_to_tuple


import sys


class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.map_image = None

    def render_map(self, map_image):
        image_pixmap = QPixmap('data/' + map_image)
        self.map_label.setPixmap(image_pixmap)
        self.map_label.show()


class Maps:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.gui = GUI()
        self.coordinates = None  # (float, float)
        self.scale = None  # (float, float)

    def set_coordinates(self, *args):  # установка координат
        self.coordinates = fetch_to_tuple(args)

    def set_scale(self, *args):  # установка масштаба
        self.scale = fetch_to_tuple(args)



    def get_map_image(self):
        map_image = geo.get_map_image(self.coordinates, self.scale)
        return map_image

    def run(self):
        # start code

        map_image = self.get_map_image()
        self.gui.render_map(map_image)

        # end code

        self.gui.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    main = Maps()
    main.set_coordinates([5.326767, 7.398632])
    main.set_scale(10, 10)
    main.run()
