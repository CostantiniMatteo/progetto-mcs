import numpy as np
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm
from scipy.fftpack import dct, idct

#img = np.random.randint(0,255,25).reshape(5,5)

# Lettura immagine
img = cv2.imread('immagini/artificial.bmp')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Inserimento valori
beta = int(input('Inserisci beta: '))

d = sum(img.shape)
while d > sum(img.shape) - 2:
    d = int(input('Inserisci d: '))


# Applicazione dct
d_img = dct(img, norm='ortho')

# modifica frequenze
for i, row in tqdm(enumerate(d_img)):
  for j, col in enumerate(row):
    if i + j >= d:
        d_img[i, j] *= beta


# Applicazione inversa dct
i_img = idct(d_img, norm='ortho')


# Arrotondamento
for i, row in tqdm(enumerate(i_img)):
  for j, col in enumerate(row):

    if i_img[i, j] > 255:
        i_img[i, j] = 255
    elif i_img[i, j] < 0:
        i_img[i, j] = 0
    else:
        i_img[i, j] = round(i_img[i, j])


# Visualizzazione
plt.imshow(i_img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.show()
