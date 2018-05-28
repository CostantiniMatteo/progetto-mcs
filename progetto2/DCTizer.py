import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QDoubleValidator, QIntValidator
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
        self.height = 270

        self.initUI()


    def initUI(self):

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('DCTizer')
        self.setWindowIcon(QIcon('icon.png'))

        # Textbox path
        self.textboxPath = QLineEdit(self)
        self.textboxPath.move(20, 20)
        self.textboxPath.resize(550,40)
        self.textboxPath.setReadOnly(True)

        # Textbox Beta
        self.textboxBeta = QLineEdit(self)
        self.textboxBeta.move(20, 80)
        self.textboxBeta.resize(80, 40)
        self.onlyDouble = QDoubleValidator()
        self.textboxBeta.setValidator(self.onlyDouble)

        # Label Beta
        self.labelBeta = QLabel("Valore di β", self)
        self.labelBeta.move(130, 90)

        # Textbox d
        self.textboxD = QLineEdit(self)
        self.textboxD.move(300, 80)
        self.textboxD.resize(80, 40)
        self.onlyInt = QIntValidator()
        self.textboxD.setValidator(self.onlyInt)

        # Label d
        self.labelD = QLabel("Valore di d", self)
        self.labelD.move(410, 90)


        # Button path
        buttonPath = QPushButton('Carica immagine', self)
        buttonPath.setToolTip('Apertura finestra di ricerca file')
        buttonPath.move(580,30)
        buttonPath.clicked.connect(self.on_click_path)


        # Button alter freq
        buttonAlter = QPushButton('Make the Magic', self)
        buttonAlter.setToolTip('This is an example button')
        buttonAlter.move(20, 210)
        buttonAlter.resize(680, 40)
        buttonAlter.clicked.connect(self.on_click_alter_freq)

        # Progress bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(20, 150, 680, 30)
        self.progress.setValue(0)
        self.progress.hide()

        # Inizializzazione
        # fileName = '/home/dario/git/progetto-mcs/progetto2/immagini/grey/artificial.bmp'
        # self.textboxPath.setText(fileName)
        # self.textboxD.setText('500')
        # self.textboxBeta.setText('0')
        # self.d_max = 1278
        # self.img = cv2.imread(fileName)
        # self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY).astype(float)

        self.show()


    @pyqtSlot()
    def on_click_path(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,"QFileDialog.getOpenFileName()", "","Images (*.png *.jpg *.jpeg *.bmp)",
            options=options
        )

        if fileName:
            self.textboxPath.setText(fileName)
            self.img = cv2.imread(fileName)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY).astype(float)
            self.d_max = sum(self.img.shape) - 2
            self.labelD.setText(f"Valore di d < {self.d_max}")
            self.labelD.hide()
            self.labelD.show()


    @pyqtSlot()
    def on_click_alter_freq(self):
        try:
            self.d = int(self.textboxD.text())
            self.beta = float(self.textboxBeta.text())
        except Exception:
            QMessageBox.about(
                self,
                'Error',
                f"Valore di d oppure β non valido"
            )

            return

        if not self.textboxPath.text():
            QMessageBox.about(
                self,
                'Error',
                'Percorso immagine non valido'
            )

            return

        if self.d > self.d_max:
            QMessageBox.about(
                self,
                'Error',
                f"d deve essere minore di {self.d_max}"
            )

            return

        elif self.d < 0:
            QMessageBox.about(
                self,
                'Error',
                f"d deve essere maggiore di 0"
            )

            return

        self.alter_freq()


    def round_image_(self, pixel):
        if pixel > 255:
            return 255
        elif pixel < 0:
            return 0
        else:
            return round(pixel)


    def alter_freq(self):
        self.progress.setValue(0)
        self.progress.show()

        round_image = np.vectorize(self.round_image_)

        # Applicazione dct
        d_img = dct(dct(self.img.T, norm='ortho').T, norm='ortho')

        self.progress.setValue(25)

        # modifica frequenze
        for i, row in enumerate(d_img):
            self.progress.setValue(26 + (45 * i) / d_img.shape[0])
            for j, col in enumerate(row):
                if i + j >= self.d:
                    d_img[i, j] *= self.beta


        # Applicazione inversa dct e arrotondamento
        i_img = round_image(idct(idct(d_img.T, norm='ortho').T, norm='ortho'))


        self.progress.setValue(self.progress.value() + 25)

        plt.figure(1)
        # Visualizzazione
        plt.subplot(122)
        plt.imshow(i_img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
        plt.title('Immagine alterata')

        plt.subplot(121)
        plt.imshow(self.img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
        plt.title('Immagine originale')

        fig = plt.gcf()
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))
        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())

        self.progress.setValue(self.progress.value() + 5)

        plt.figure(2)
        sub_img = cv2.absdiff(self.img, i_img.astype(float))
        plt.imshow(sub_img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
        plt.title('Immagine differenza')

        plt.show()

