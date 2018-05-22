import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from scipy.fftpack import dct, idct
import cv2
import numpy as np
import matplotlib.pyplot as plt


class DCTizer(QWidget):

    def __init__(self):
        super().__init__()

        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 730
        self.height = 220

        self.initUI()


    def initUI(self):

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))

        # Textbox path
        self.textboxPath = QLineEdit(self)
        self.textboxPath.move(20, 20)
        self.textboxPath.resize(550,40)

        # Textbox Beta
        self.textboxBeta = QLineEdit(self)
        self.textboxBeta.move(20, 80)
        self.textboxBeta.resize(80, 40)

        # Label Beta
        self.labelBeta = QLabel("Valore di Beta", self)
        self.labelBeta.move(130, 90)

        # Textbox d
        self.textboxD = QLineEdit(self)
        self.textboxD.move(300, 80)
        self.textboxD.resize(80, 40)

        # Label d
        self.labelD = QLabel("Valore di d", self)
        self.labelD.move(410, 90)


        # Button path
        buttonPath = QPushButton('Carica immagine', self)
        buttonPath.setToolTip('Apertura finestra di ricerca file')
        buttonPath.move(580,30)
        buttonPath.clicked.connect(self.on_click_path)


        # Button alter freq
        buttonAlter = QPushButton('Applica alterazione frequenze', self)
        buttonAlter.setToolTip('This is an example button')
        buttonAlter.move(20,160)
        buttonAlter.resize(680, 40)
        buttonAlter.clicked.connect(self.alter_freq)


        self.show()


    @pyqtSlot()
    def on_click_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)",
            options=options
        )

        if fileName:
            self.textboxPath.setText(fileName)
            self.img = cv2.imread(fileName)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            d_max = sum(self.img.shape) - 2
            new_text = f"{self.labelD.text()} minore {d_max}"
            print(new_text)
            #self.labelD.setText('ciao')
            self.labelD.setText(f"{self.labelD.text()} minore {d_max}")


    def round_image_(pixel):
        if pixel > 255:
            return 255
        elif pixel < 0:
            return 0
        else:
            return round(pixel)


    def alter_freq(path):


        # Inserimento valori
        beta = int(input('Inserisci beta: '))

        d = sum(img.shape)
        while d > sum(img.shape) - 2:
            d = int(input('Inserisci d: '))


        round_image = np.vectorize(round_image_)

        # Applicazione dct
        d_img = dct(dct(img.T, norm='ortho').T, norm='ortho')

        # modifica frequenze
        for i, row in tqdm(enumerate(d_img)):
          for j, col in enumerate(row):
            if i + j >= d:
                d_img[i, j] *= beta


        # Applicazione inversa dct e arrotondamento
        i_img = round_image(idct(idct(d_img.T, norm='ortho').T, norm='ortho'))


        # Visualizzazione
        plt.imshow(i_img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
        plt.show()
