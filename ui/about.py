# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AboutWindow(QWidget):
    """Help window"""
    def __init__(self, parent=None):
        """Constructor"""
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        """Setup User Interface"""
        self.setObjectName("About")
        self.setWindowTitle(u"About")

        vertLayout = QVBoxLayout(self)
        vertLayout.setObjectName("vertLayout")

        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        scrollArea.setObjectName("scrollArea")
        
        scrollAreaWidgetContents = QWidget()
        scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        gridLayout = QGridLayout(scrollAreaWidgetContents)

        plainTextEdit = QPlainTextEdit(scrollAreaWidgetContents)
        plainTextEdit.setObjectName("plainTextEdit")
        plainTextEdit.setPlainText(u"Здесь описание программы")

        gridLayout.addWidget(plainTextEdit, 0, 0, 1, 1)
        scrollArea.setWidget(scrollAreaWidgetContents)
        vertLayout.addWidget(scrollArea)
        
        okButton = QPushButton(self)
        okButton.setMaximumSize(QSize(80, 25))
        okButton.setObjectName("okButton")
        okButton.setText(u"&Close")
        okButton.pressed.connect(self.closeWindow)
        vertLayout.addWidget(okButton, 0, Qt.AlignRight)
        pass
        
    def closeWindow(self):
        self.close()
    
