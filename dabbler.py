from PyQt5.QtWidgets import QFileDialog, QWidget, QAction, QMessageBox
from krita import *

DOCKER_TITLE = 'Blank Template Docker'

class DockerDabbler(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle(DOCKER_TITLE)

    # notifies when views are added or removed
    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass

class ExtensionTemplate(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def system_check(self):
        # QMessageBox creates quick popup with information
        messageBox = QMessageBox()
        messageBox.setInformativeText(Application.version())
        messageBox.setWindowTitle('System Check')
        messageBox.setText("Hello! Here is the version of Krita you are using.");
        messageBox.setStandardButtons(QMessageBox.Close)
        messageBox.setIcon(QMessageBox.Information)
        messageBox.exec()

    def createActions(self, window):
        action = window.createAction("", "System Check")
        action.triggered.connect(self.system_check)