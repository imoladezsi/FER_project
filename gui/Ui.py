from PyQt5 import QtWidgets, uic, QtCore,  QtGui
from os.path import expanduser
from PyQt5.QtWidgets import *

import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('MainWindow.ui', self) # Load the .ui file
        self.show() # Show the GUI

    def getDirectory(self):
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"), QFileDialog.ShowDirsOnly)
        # noinspection PyTypeChecker
        label: QLabel = self.findChild(QtWidgets.QLabel, 'dirLabel')
        label.setText(dir_)
        print(dir_)

    def train(self):
        pass

    def setDirectory(self):
        pass