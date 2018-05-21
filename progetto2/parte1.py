import numpy as np
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
from scipy.fftpack import dct, idct


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



mat = np.array([[ 95, 251, 154, 130,  89],
                [209,  65,  50, 183, 224],
                [ 38, 157,  31,  35, 131],
                [  7, 137, 113, 118,  81],
                [138,  32,  95, 132, 185]])

test_mat = np.array([[231, 32, 233, 161, 24, 71, 140, 245],
                  [247, 40, 248, 245, 124, 204, 36, 107],
                  [234, 202, 245, 167, 9, 217, 239, 173],
                  [193, 190, 100, 167, 43, 180, 8, 70],
                  [11, 24, 210, 177, 81, 243, 8, 112],
                  [97, 195, 203, 47, 125, 114, 165, 181],
                  [193, 70, 174, 167, 41, 30, 127, 245],
                  [87, 149, 57, 192, 65, 129, 178, 228]])
