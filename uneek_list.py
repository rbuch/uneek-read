#! /usr/bin/env python

import sys

def inList(genes, value):
    global counter
    while counter < len(genes) and genes[counter] < value:
        counter = counter + 1
    return counter < len(genes) and genes[counter] == value

def parseLine(line):
    first, _ = line.split(None, 1)
    first = first[14:].split('#')[0].split(':')
    first[2] = first[2].zfill(6)

    return int(''.join(first))

if len(sys.argv) < 3:
    print "You must supply at least two file names: ./uneek.py file1 file2 ..."
    sys.exit(1)

genes = list()

for index in range(1, len(sys.argv)):
    counter = 0
    with open(sys.argv[index], 'r') as f:
        for line in f:
            if line[0] == '@':
                continue
            value = parseLine(line)

            if index == 1:
                genes.append(value)
            elif not inList(genes, value):
                sys.stdout.write(line)

