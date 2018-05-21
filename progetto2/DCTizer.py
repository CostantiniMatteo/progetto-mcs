import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class DCTizer(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 730
        self.height = 300

        self.initUI()


    def initUI(self):

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        # Textbox path
        self.textboxPath = QLineEdit(self)
        self.textboxPath.move(20, 20)
        self.textboxPath.resize(550,40)

        # Textbox d
        self.textboxD = QLineEdit(self)
        self.textboxD.move(20, 80)
        self.textboxD.resize(80, 40)

        # Label d
        self.labelD = QLabel("Valore di d", self)
        self.labelD.move(130, 90)

        # Textbox beta
        self.textboxBeta = QLineEdit(self)
        self.textboxBeta.move(20, 140)
        self.textboxBeta.resize(80, 40)

        # Label d
        self.labelBeta = QLabel("Valore di Beta", self)
        self.labelBeta.move(130, 150)


        # Button path
        button = QPushButton('Carica immagine', self)
        button.setToolTip('This is an example button')
        button.move(580,30)
        button.clicked.connect(self.on_click)

        self.show()


    @pyqtSlot()
    def on_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)",
            options=options
        )

        if fileName:
            self.textboxPath.setText(fileName)
