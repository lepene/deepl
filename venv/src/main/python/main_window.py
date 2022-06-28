from PySide2 import QtWidgets
import deepl

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Deepl")
        self.resize(250, 150)
