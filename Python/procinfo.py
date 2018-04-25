#!/usr/bin/env python

import argparse
import sys

import psutil

def convert_bytes(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.3f%s' % (value, s)
    return "%sB" % n


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="print information about a process")
    parser.add_argument("pid", type=int, help="process pid")
    parser.add_argument('--verbose', '-v', action='store_true',
                        help="print more info")
    args = parser.parse_args()
    # run(args.pid, args.verbose)

    try:
        proc = psutil.Process(args.pid)
        import time
        while True:
            time.sleep(0.1)
            pinfo = proc.as_dict(ad_value='')
            print(convert_bytes(pinfo['memory_info'][0]))
    except psutil.NoSuchProcess as err:
        sys.exit(str(err))



if __name__ == '__main__':
    sys.exit(main())
