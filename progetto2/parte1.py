import numpy as np
import math
from scipy.fftpack import dctn
from numba import jit
import sys


TEST_MAT = np.array([[231,  32, 233, 161,  24,  71, 140, 245],
                     [247,  40, 248, 245, 124, 204,  36, 107],
                     [234, 202, 245, 167,   9, 217, 239, 173],
                     [193, 190, 100, 167,  43, 180,   8,  70],
                     [ 11,  24, 210, 177,  81, 243,   8, 112],
                     [ 97, 195, 203,  47, 125, 114, 165, 181],
                     [193,  70, 174, 167,  41,  30, 127, 245],
                     [ 87, 149,  57, 192,  65, 129, 178, 228]])


# 1-Dimensional DCT implemented as seen during lectures
@jit
def custom_dct(array):
    r_array = np.zeros(array.size)
    N = array.size

    for u in range(N):
        somma = 0
        a = math.sqrt(1. / N) if u == 0 else math.sqrt(2. / N)

        for x, cell in enumerate(array):
            somma += cell * math.cos((u * math.pi * (2 * x + 1)) / (2 * N))

        r_array[u] = a * somma

    return r_array


# 2-Dimensional DCT coputed by applying row*column 1-D DCTs
@jit
def custom_dct2(mat):
    r_mat = np.zeros(mat.shape)
    r_mat = np.apply_along_axis(custom_dct, axis=1, arr=mat)
    r_mat = np.apply_along_axis(custom_dct, axis=0, arr=r_mat)

    return r_mat



if __name__ == '__main__':
    import sys, cv2
    from datetime import datetime
    from tqdm import tqdm
    from os import listdir
    from os.path import exists, abspath, join

    if len(sys.argv) < 4:
        sys.exit(f"Usage: {sys.argv[0]} n_min n_max step\
All arguments must be integers.")

    try:
        begin = int(sys.argv[1])
        end = int(sys.argv[2])
        step = int(sys.argv[3])
    except:
        sys.exit(f"Usage: {sys.argv[0]} n_min n_max step\
All arguments must be integers.")

    # print("rows,custom,scipy")
    for N in tqdm(range(begin, end+1, step)):
            img = np.random.uniform(low=0.0, high=255.0, size=(N, N))

            t_start = datetime.now()
            custom_res = custom_dct2(img)
            end_custom = (datetime.now() - t_start).total_seconds()

            t_start = datetime.now()
            scipy_res = dctm(img, norm='ortho')
            end_scipy = (datetime.now() - t_start).total_seconds()

            print(f"{N},{end_custom},{end_scipy}")
