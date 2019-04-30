# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maps_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 515)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.map_frame = QtWidgets.QFrame(self.centralwidget)
        self.map_frame.setGeometry(QtCore.QRect(20, 50, 581, 411))
        self.map_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.map_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.map_frame.setLineWidth(3)
        self.map_frame.setObjectName("map_frame")
        self.map_label = QtWidgets.QLabel(self.map_frame)
        self.map_label.setGeometry(QtCore.QRect(6, 22, 571, 401))
        self.map_label.setText("")
        self.map_label.setObjectName("map_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(480, 10, 121, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sat_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sat_btn.setObjectName("sat_btn")
        self.horizontalLayout.addWidget(self.sat_btn)
        self.map_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.map_btn.setObjectName("map_btn")
        self.horizontalLayout.addWidget(self.map_btn)
        self.hyb_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hyb_btn.setObjectName("hyb_btn")
        self.horizontalLayout.addWidget(self.hyb_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sat_btn.setText(_translate("MainWindow", "SAT"))
        self.map_btn.setText(_translate("MainWindow", "MAP"))
        self.hyb_btn.setText(_translate("MainWindow", "HYB"))

