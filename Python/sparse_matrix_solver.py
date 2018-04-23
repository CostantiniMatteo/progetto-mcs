import numpy as np
import scipy
import scipy.io

def solve(A, b):
    n_rows, n_columns = A.shape
    xe = np.ones(n_rows)
    b = A * xe

def read_matrix(path):
    A = scipy.io.mmread(path)
