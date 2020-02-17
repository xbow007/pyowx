#!/usr/bin/python3
#
# -*- coding: utf-8 -*-
#
#


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *

import ui
# from ui import *

import sys

try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except Exception:
    pass


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        self.name = "pyowx"
        self.setupUi()

    def setupUi(self):
        """Setup User Interface"""
        self.centralWidget = QWidget()
        mbar = self.menuBar()

        file_menu = mbar.addMenu(u"&Файл")
        open_action = QAction(u"&Открыть", self)
        close_action = QAction(u"&Закрыть", self)
        file_menu.addAction(open_action)
        file_menu.addAction(close_action)
        close_action.triggered.connect(self.Quitaction)
        # ----------------------------------------------
        edit_menu = mbar.addMenu(u"&Правка")
        undo_action = QAction(u"&Undo", self)
        edit_menu.addAction(undo_action)
        config_action = QAction(u"&Настройка", self)
        edit_menu.addAction(config_action)
        undo_action.triggered.connect(self.undoAction)
        config_action.triggered.connect(self.configAction)



    def Quitaction(self):
        """Quit from MainWindow"""
        print("Quit from MainWindow")
        self.close()

    def undoAction(self):
        pass

    def configAction(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.setWindowTitle(u"PyOWX")
    mainwindow.resize(1200, 500)
    mainwindow.show()
    sys.exit(app.exec())

