import numpy as np
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.fftpack import dct, idct



TEST_MAT = np.array([[231, 32, 233, 161, 24, 71, 140, 245],
                     [247, 40, 248, 245, 124, 204, 36, 107],
                     [234, 202, 245, 167, 9, 217, 239, 173],
                     [193, 190, 100, 167, 43, 180, 8, 70],
                     [11, 24, 210, 177, 81, 243, 8, 112],
                     [97, 195, 203, 47, 125, 114, 165, 181],
                     [193, 70, 174, 167, 41, 30, 127, 245],
                     [87, 149, 57, 192, 65, 129, 178, 228]])


def custom_alfa(u, N):
    if u == 0:
        return math.sqrt(1/N)
    elif u != 0:
        return math.sqrt(2/N)


def custom_dct(array):
    r_array = np.zeros(array.size)
    N = array.size


    for u in range(N):
        somma = 0
        alfa = custom_alfa(u, N)

        for x, cell in enumerate(array):
            somma += cell * math.cos((u*math.pi*(2*x + 1)) / (2*N))

        r_array[u] = alfa*somma

    return r_array


def custom_dct2(mat):
    r_mat = np.zeros(mat.shape)

    r_mat = np.apply_along_axis(custom_dct, axis=1, arr=mat)
    r_mat = np.apply_along_axis(custom_dct, axis=1, arr=r_mat.T)

    return r_mat.T

def scipy_dct2(mat):
    return dct(dct(mat.T, norm='ortho').T, norm='ortho')



if __name__ == '__main__':
    import sys, cv2
    from datetime import datetime
    from os import listdir

    PATH = 'immagini/grey'
    if len(sys.argv > 1):
        PATH = sys.argv[1]

    for file in tqdm(os.listdir(PATH)):
        if file.endswith('.bmp'):
            img = cv2.imread('immagini/artificial.bmp')
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            t_start = datetime.now()
            custom_res = custom_dct2(img)
            end_custom = (datetime.now() - t_start).total_seconds()

            t_start = datetime.now()
            scipy_res = scipy_dct2(img)
            end_scipy = (datetime.now() - t_start).total_seconds()

            print(f"{file.split('.')[0]},{end_custom},{end_scipy}")

