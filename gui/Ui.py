from PyQt5 import QtWidgets, uic
from os.path import expanduser
from PyQt5.QtWidgets import *


class Ui(QtWidgets.QMainWindow):
    def __init__(self, face_det_repo, fer_repo):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        self.current_fd = None
        self.current_fer = None

        self.directory_path = None
        self.fd_repo = face_det_repo
        self.fer_repo = fer_repo
        self.window = uic.loadUi('MainWindow.ui', self)  # Load the .ui file
        self.set_up_UI()
        self.show()  # Show the GUI

    def set_up_UI(self):
        options = self.fd_repo.get_options()
        self.window.faceDetComboBox.addItems(options)
        self.current_fd = options[0]
        options = self.fer_repo.get_options()
        self.window.modelComboBox.addItems(options)
        self.current_fer = options[0]
        # signals and slots
        self.window.faceDetComboBox.currentIndexChanged.connect(self.onFDComboBoxChanged, self.window.faceDetComboBox.currentIndex())
        self.window.modelComboBox.currentIndexChanged.connect(self.onFERComboBoxChanged, self.window.modelComboBox.currentIndex())

    # noinspection PyArgumentList

    def getDirectory(self):
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"), QFileDialog.ShowDirsOnly)
        self.window.dirLabel.setText(dir_)
        self.directory_path = dir_

    def train(self):
        self.current_fer.set_params()

    def setDirectory(self):
        pass

    def onFDComboBoxChanged(self, index):
        options = self.fd_repo.get_options()
        self.current_fd = options[index]
        print(options[index])

    def onFERComboBoxChanged(self, index):
        options = self.fer_repo.get_options()
        self.current_fer = options[index]
        print(options[index])

