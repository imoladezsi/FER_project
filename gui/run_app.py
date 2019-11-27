
import sys
from PyQt5 import QtWidgets

from Ui import Ui

app = QtWidgets.QApplication(sys.argv)

window = Ui()

# Start the event loop.
app.exec_()

