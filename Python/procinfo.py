#!/usr/bin/env python

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


# ./procinfo.py 0.5 $(pgrep -f pattern)
if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit("Missing PID")

    delay = 1 if len(sys.argv) < 3 else float(sys.argv[1])
    pid = int(sys.argv[1]) if len(sys.argv) == 2 else int(sys.argv[2])

    print('###########################################################')
    print('###########################################################')
    print('###########################################################')
    try:
        proc = psutil.Process(pid)
        import time
        i = 0
        while True:
            time.sleep(delay)
            pinfo = proc.as_dict(ad_value='')
            print(convert_bytes(pinfo['memory_info'][0]))
    except psutil.NoSuchProcess as err:
        sys.exit(str(err))
