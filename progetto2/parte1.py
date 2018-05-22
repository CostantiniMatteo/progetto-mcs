import numpy as np
import math
from scipy.fftpack import dct, idct



TEST_MAT = np.array([[231,  32, 233, 161,  24,  71, 140, 245],
                     [247,  40, 248, 245, 124, 204,  36, 107],
                     [234, 202, 245, 167,   9, 217, 239, 173],
                     [193, 190, 100, 167,  43, 180,   8,  70],
                     [ 11,  24, 210, 177,  81, 243,   8, 112],
                     [ 97, 195, 203,  47, 125, 114, 165, 181],
                     [193,  70, 174, 167,  41,  30, 127, 245],
                     [ 87, 149,  57, 192,  65, 129, 178, 228]])


# 1-Dimensional DCT implemented as seen during lectures
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
def custom_dct2(mat):
    r_mat = np.zeros(mat.shape)

    r_mat = np.apply_along_axis(custom_dct, axis=1, arr=mat)
    r_mat = np.apply_along_axis(custom_dct, axis=0, arr=r_mat)

    return r_mat


# Utility wrapper
def scipy_dct2(mat):
    return dct(dct(mat, norm='ortho', axis=0), norm='ortho', axis=1)



if __name__ == '__main__':
    import sys, cv2
    from datetime import datetime
    from tqdm import tqdm
    from os import listdir
    from os.path import exists, abspath, join

    PATH = 'immagini/grey/immagini-artificiali'
    if len(sys.argv) > 1:
        if sys.argv[1] != '-d': PATH = sys.argv[1]
    else:
        print(f"Using default directory ({PATH}).", file=sys.stderr)
        print("Use -d to suppress this message or pass another\
path as argument", file=sys.stderr)

    if not exists(PATH):
        sys.exit("Source directory does not exist!")

    print("name,custom,scipy")
    for file in tqdm(sorted(listdir(PATH))):
        if file.endswith('.bmp'):
            img = cv2.imread(abspath(join(PATH, file)))
            # Cast as float because otherwise it will use numpy's uint8
            # which are mapped to C's uint8. This will lead to a lot of
            # overhead in the conversion from uint8 to int, then to
            # float and then back to uint8 again when computing custom_dct
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(float)

            t_start = datetime.now()
            custom_res = custom_dct2(img)
            end_custom = (datetime.now() - t_start).total_seconds()

            t_start = datetime.now()
            scipy_res = scipy_dct2(img)
            end_scipy = (datetime.now() - t_start).total_seconds()

            print(f"{file.split('.')[0]},{end_custom},{end_scipy}")
