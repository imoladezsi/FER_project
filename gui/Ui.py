import os

from PyQt5 import QtWidgets, uic
from os.path import expanduser
from PyQt5.QtWidgets import *
import logging

from face_detection import FaceDetectionInterface
from facial_expression_recognition.ModelInterface import  ModelInterface
from facial_expression_recognition.FerAPI import FerAPI


class Ui(QtWidgets.QMainWindow):
    def __init__(self, face_det_repo, fer_repo):
        super(Ui, self).__init__() # Call the inherited classes __init__ method

        self.directory_path = None
        self.save_to = None
        self.fd_repo = face_det_repo
        self.fer_repo: FerAPI = fer_repo
        self.fer_options = self.fer_repo.get_options()
        self.fd_options = self.fd_repo.get_options()
        self.current_fd: FaceDetectionInterface = None
        self.current_fer: ModelInterface = None

        self.window = uic.loadUi('MainWindow.ui', self)  # Load the .ui file
        self.set_up_UI()
        self.show()  # Show the GUI

    def set_up_UI(self):
        labels = self.fd_repo.get_labels()
        self.window.faceDetComboBox.addItems(labels)
        self.current_fd = self.fd_options[0]
        labels = self.fer_repo.get_labels()
        self.window.modelComboBox.addItems(labels)
        self.current_fer: ModelInterface = self.fer_options[0]

        # set default values. These should probably be elsewhere
        self.window.learningRateLineEdit.setText(str(self.current_fer.get_init_lr()))
        self.window.dropoutLineEdit.setText(str(self.current_fer.get_dropout()))
        self.window.imgDimLineEdit.setText(str(self.current_fer.get_img_dim()))
        self.window.batchSizeLineEdit.setText(str(self.current_fer.get_batch_size()))
        self.window.epochsLineEdit.setText(str(self.current_fer.get_epochs()))
        self.window.splitLineEdit.setText(str(self.current_fer.get_split()))

        # signals and slots
        self.window.faceDetComboBox.currentIndexChanged.connect(self.onFDComboBoxChanged, self.window.faceDetComboBox.currentIndex())
        self.window.modelComboBox.currentIndexChanged.connect(self.onFERComboBoxChanged, self.window.modelComboBox.currentIndex())

    def get_classes(self):
        # should not be any empty directory
        for _, dirnames, _ in os.walk(self.directory_path):
            return dirnames

    def getDirectory(self):
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"), QFileDialog.ShowDirsOnly)
        self.window.dirLabel.setText(dir_)
        self.directory_path = dir_


    def train(self):
        try:
            img_dim = int(self.window.imgDimLineEdit.text())
            dropout = float(self.window.dropoutLineEdit.text())
            init_lr = float(self.window.learningRateLineEdit.text())
            batch_size = int(self.window.batchSizeLineEdit.text())
            classes = self.get_classes()
            depth = 3
            epochs = int(self.window.epochsLineEdit.text())
            split = int(self.window.splitLineEdit.text())
            self.current_fer.set_params(img_dim, dropout, init_lr, len(classes), depth, batch_size, epochs)
            self.current_fer.initialize_model()

            lb, model = FerAPI.train(self.current_fer, self.current_fd, self.directory_path, img_dim, split, epochs, batch_size)

            # default save to location
            if self.save_to is None:
                self.save_to = os.path.join(os.path.dirname(os.path.abspath(__file__)),"output")
                if not os.path.exists(self.save_to):
                    os.mkdir(self.save_to)

            FerAPI.save_training_data(self.current_fer, lb, self.save_to, self.current_fer.get_name(), epochs)
        except Exception as e:
            logging.exception("Error")

    def setDirectory(self):
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"), QFileDialog.ShowDirsOnly)
        self.save_to = dir_

    def onFDComboBoxChanged(self, index):
        self.current_fd = self.fd_options[index]

    def onFERComboBoxChanged(self, index):
        self.current_fer = self.fer_options[index]



