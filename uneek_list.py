#! /usr/bin/env python

import sys
import hashlib
import bisect

def inList(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False

if len(sys.argv) < 3:
    print "You must supply at least two file names: ./uneek.py file1 file2 ..."
    sys.exit(1)

genes = list()

for index in range(1, len(sys.argv)):
    with open(sys.argv[index], 'r') as f:
        for line in f:
            if line[0] == '@':
                continue
            first, second, _ = line.split(None, 2)
            second.zfill(3)
            value = int(first[14:].split('#')[0].replace(':', '') + second)

            if index == 1:
                genes.append(value)
            elif inList(genes, value):
                sys.stdout.write(line)
