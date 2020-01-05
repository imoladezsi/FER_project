
import sys
from PyQt5 import QtWidgets

from Ui import Ui
from face_detection.CVFaceCascade import CVFaceCascade
from face_detection.FaceDetectionAPI import FaceDetectionAPI
from facial_expression_recognition.FerAPI import FerAPI
from facial_expression_recognition.SampleModel1 import SampleModel1
from facial_expression_recognition.SampleModel2 import SampleModel2
import os

proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cascade_path = os.path.join(proj_path, "venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

app = QtWidgets.QApplication(sys.argv)

fd_algs = [
           CVFaceCascade(cascade_path)]
fd_repo = FaceDetectionAPI(fd_algs)

fer_models = [SampleModel1(), SampleModel2(),]
fer_repo = FerAPI(fer_models)


window = Ui(fd_repo, fer_repo)

# Start the event loop.
app.exec_()

