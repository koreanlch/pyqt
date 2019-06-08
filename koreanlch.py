#-*- coding:utf-8 -*-

import sys
#PyQt must be installed.

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

formClass = uic.loadUiType('koreanlch.ui')[0]

class MainformClass(QMainWindow, formClass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textedit.textChanged.connect(self.hohohoho)
        self.pushButton.clicked.connect(self.hahahaha)

    def hohohoho(self):
        wow = self.textedit.toPlainText()
        self.label.setText(wow)

    def hahahaha(self) :
        wow = self.textedit.toPlainText()
        self.label.setText(str(eval(wow)))
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainformClass()
    mainWindow.show()
    app.exec_()
