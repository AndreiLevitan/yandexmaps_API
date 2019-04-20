from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from maps_gui import Ui_MainWindow
from requester import geo

from tips import fetch_to_tuple


import sys
import logging


class GUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.map_image = None
        logging.info('Initialized GUI')

    def render_map(self, map_image):
        image_pixmap = QPixmap('data/' + map_image)
        self.map_label.setPixmap(image_pixmap)
        self.map_label.show()
        logging.info('Showed map image %r', map_image)

    def keyPressEvent(self, event):
        PGUP = 16777238  # константа клавиши PgUp
        PGDN = 16777239  # константа клавиши PgDn
        if event.key() == PGDN:  # отлов ивентов клавиш
            main.scale_down()
        elif event.key() == PGUP:
            main.scale_up()


class Maps:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.gui = GUI()
        self.coordinates = None  # (float, float)
        self.scale = None  # (float, float)
        self.gui.show()
        logging.info('Initialized Maps')

    def set_coordinates(self, *args):  # установка координат
        self.coordinates = fetch_to_tuple(args)
        logging.info('Set coordinates to %r', self.coordinates)

    def set_scale(self, *args):  # установка масштаба
        self.scale = fetch_to_tuple(args)
        logging.info('Set scale to %r', self.scale)

    def get_map_image(self):
        map_image = geo.get_map_image(self.coordinates, self.scale)
        logging.info('Get image %r', map_image)
        return map_image

    def scale_up(self):
        self.scale = (min(max(self.scale[0] * 2, 0.15625), 80),  # значение между scale 0.15625 и 80
                      min(max(self.scale[1] * 2, 0.15625), 80))
        self.init_map()  # реинициализация карты
        logging.info('Set scale up to %r', self.scale)

    def scale_down(self):
        self.scale = (min(max(self.scale[0] / 2, 0.15625), 80),  # значение между scale 0.15625 и 80
                      min(max(self.scale[1] / 2, 0.15625), 80))
        self.init_map()  # реинициализация карты
        logging.info('Set scale down to %r', self.scale)

    def init_map(self):  # инициализация и отображение карты
        map_image = self.get_map_image()
        self.gui.render_map(map_image)

    def run(self):
        logging.info('Run app...')

        # start code

        self.init_map()

        # end code


        self.gui.show()
        self.terminate()

    def terminate(self):
        logging.info('Run finished')
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main = Maps()
    main.set_coordinates('5.326767', '7.398632')
    main.set_scale(10, 10)
    main.run()
