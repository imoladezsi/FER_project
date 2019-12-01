
import sys
from PyQt5 import QtWidgets

from Ui import Ui
from face_detection.FaceDetectionRepository import FaceDetectionRepository
from face_detection.ViolaJones import ViolaJones
from facial_expression_recognition.FerRepository import FerRepository
from facial_expression_recognition.SampleModel1 import SampleModel1
from facial_expression_recognition.SampleModel2 import SampleModel2

app = QtWidgets.QApplication(sys.argv)

fd_algs = [ViolaJones(""),]
fd_repo = FaceDetectionRepository(fd_algs)

fer_models = [SampleModel1(), SampleModel2(),]  # TODO: use something like the class FER for this, to call its methods and make them common
fer_repo = FerRepository(fer_models)


window = Ui(fd_repo, fer_repo)

# Start the event loop.
app.exec_()

