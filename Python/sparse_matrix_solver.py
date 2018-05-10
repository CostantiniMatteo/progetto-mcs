#! /usr/bin/env python3

from datetime import datetime

import scipy, scipy.io
from scipy.sparse.linalg import norm, spsolve
from scipy.linalg import norm



def solve(A, use_umfpack=False):
    # Compute b such that the exact solution of Ax = b is xe = [1, 1, ...]
    n_rows, n_columns = A.shape
    p_non_zero = A.nnz / (n_rows * n_columns)
    xe = scipy.ones(n_rows)
    b = A * xe

    # Solve Ax = b
    start_time = datetime.now()
    x = solve_aux(A, b, use_umfpack=use_umfpack)
    t = datetime.now() - start_time

    # || xe - x || / ||xe||
    relative_error = norm(x - xe, 2) / norm(xe, 2)

    print("Shape: {} x {}".format(n_rows, n_columns))
    if p_non_zero < 0.00001:
        print("Non-zero: {} (< 0.00001%)".format(A.nnz))
    else:
        print("Non-zero: {0} ({1:.5f}%)".format(A.nnz, p_non_zero))
    print("Relative error: {}".format(relative_error))
    print(f"Time (solve): {t} ({t.seconds}.{t.microseconds}s)")
    row = f"{args.MAT_DIR.split('/')[-1].split('.')[0]},{n_rows},{A.nnz},{relative_error},{t.seconds}.{t.microseconds}"
    print(row)

    # Scrivo sul log
    with open("../logs/res.log", "a") as log:
        log.write(row + ',mem,1,python,windows\n')




def solve_aux(A, b, use_umfpack=False):
    x = spsolve(A, b, use_umfpack=use_umfpack)
    return x



if __name__ == "__main__":
    import sys, time, gc, argparse
    from os import listdir
    from os.path import isfile, join, exists, abspath

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

    if args.MAT_DIR.endswith('.mtx'):
        A = scipy.io.mmread(args.MAT_DIR).tocsc()
        print("================== Solving {} ==================".format(args.MAT_DIR))
        if args.interactive: sys.stdin.readline()
        x = solve(A, use_umfpack=args.use_umfpack)
        if args.interactive: sys.stdin.readline()
        sys.exit()

    for f in sorted(listdir(args.MAT_DIR)):
        path = join(args.MAT_DIR, f)
        if isfile(path) and f != '.DS_Store':
            if args.interactive: sys.stdin.readline()
            A = None; x = None; gc.collect()
            if args.interactive: sys.stdin.readline()
            time.sleep(1)
            print("================== Solving {} ==================".format(f))
            start_time = datetime.now()
            A = scipy.io.mmread(path).tocsc()
            t = datetime.now() - start_time
            print(f"Time (read): {t} ({t.seconds}.{t.microseconds}s)")
            if args.interactive: sys.stdin.readline()
            x = solve(A, use_umfpack=args.use_umfpack)
            print("")
