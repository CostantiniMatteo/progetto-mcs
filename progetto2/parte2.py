import numpy as np
import matplotlib.pyplot as plt
import cv2
from DCTizer import DCTizer
from PyQt5.QtWidgets import QApplication
import sys
from tqdm import tqdm
from scipy.fftpack import dct, idct



#img = np.random.randint(0,255,25).reshape(5,5)
def round_image_(pixel):
    if pixel > 255:
        return 255
    elif pixel < 0:
        return 0
    else:
        return round(pixel)


def alter_freq(path):

    # Lettura immagine
    # img = cv2.imread('immagini/artificial.bmp')
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


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



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = DCTizer()
    sys.exit(app.exec_())
