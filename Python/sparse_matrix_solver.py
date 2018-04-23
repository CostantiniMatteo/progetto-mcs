#! /usr/bin/env python3

from os import listdir
from os.path import isfile, join, exists, abspath
from datetime import datetime

import scipy, scipy.io
from scipy.sparse.linalg import spsolve, norm
from scipy.linalg import norm

from memory_profiler import memory_usage, profile



MAT_DIR = abspath('../Matrices')

def solve(A):
    # Compute b such that the exact solution of Ax = b is xe = [1, 1, ...]
    n_rows, n_columns = A.shape
    p_non_zero = A.nnz / (n_rows * n_columns)
    xe = scipy.ones(n_rows)
    b = A * xe

    # Solve Ax = b
    start_time = datetime.now()
    x = solve_aux(A, b)
    time = datetime.now() - start_time

    # || xe - x || / ||xe||
    relative_error = norm(x - xe, 2) / norm(xe, 2)

    print("Shape: {} x {}".format(n_rows, n_columns))
    if p_non_zero < 0.00001:
        print("Non-zero: {} (< 0.00001%)".format(A.nnz))
    else:
        print("Non-zero: {0} ({1:.5f}%)".format(A.nnz, p_non_zero))
    print("Time: {}.{}s".format(time.seconds, time.microseconds))
    print("Relative error: {}".format(relative_error))


@profile
def solve_aux(A, b):
    return spsolve(A, b)



if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        MAT_DIR = abspath(sys.argv[1])

    assert exists(MAT_DIR), "Source directory does not exist!"

    for f in sorted(listdir(MAT_DIR)):
        path = join(MAT_DIR, f)
        if isfile(path):
            print("===== Solving {} =====".format(f))
            A = scipy.io.mmread(path).tocsc()
            x = solve(A)
            print('')

