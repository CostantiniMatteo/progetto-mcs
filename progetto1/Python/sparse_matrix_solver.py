#! /usr/bin/env python3

import platform
from datetime import datetime

import scipy, scipy.io
from scipy.sparse.linalg import norm, spsolve
from scipy.linalg import norm



def solve(A, name, use_umfpack=False):
    # Compute b such that the exact solution of Ax = b is xe = [1, 1, ...]
    n_rows, n_columns = A.shape
    p_non_zero = A.nnz / (n_rows * n_columns)
    xe = scipy.ones(n_rows)
    b = A * xe

    # Solve Ax = b
    start_time = datetime.now()
    x = spsolve(A, b, use_umfpack=use_umfpack)
    t = datetime.now() - start_time

    # || xe - x || / ||xe||
    relative_error = norm(x - xe, 2) / norm(xe, 2)

    row = f"{name},{n_rows},{A.nnz},{relative_error}," + \
            f"{t.seconds}.{t.microseconds},{platform.system()}"
    print(row)



if __name__ == "__main__":
    import sys, argparse
    from tqdm import tqdm
    from os import listdir
    from os.path import join, exists, abspath

    parser = argparse.ArgumentParser()
    parser.add_argument('MAT_DIR', type=str,
        help='Directory containing .mtx files')
    parser.add_argument('--use_umfpack', '-u', action='store_true',
        help="Use umfpack library")
    parser.add_argument('--interactive', '-i', action='store_true',
        help="Wait for user input before processing a new matrix")
    args = parser.parse_args()

    if not exists(args.MAT_DIR):
        sys.exit("Source directory does not exist!")

    PATH = abspath(args.MAT_DIR)

    print('name,rows,nnz,re,time,os')
    for file in tqdm(sorted(listdir(PATH))):
        if file.endswith('.mtx'):
            A = scipy.io.mmread(join(PATH, file)).tocsc()
            if args.interactive:
                print(f"Matrix {file.split('.')[0]} loaded. Press any key...",
                    file=sys.stderr)
                sys.stdin.readline()
            x = solve(A, file.split('.')[0], use_umfpack=args.use_umfpack)
            if args.interactive:
                print("Done. Press any key...", file=sys.stderr)
                sys.stdin.readline()
