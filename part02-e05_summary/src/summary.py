#!/usr/bin/env python3

import sys
import math


def summary(filename):
    f = open(filename)
    vals = []
    for line in f:
        try:
            x = float(line)
            vals.append(x)
        except ValueError:
            continue
    summed = sum(vals)
    avg = summed/len(vals)
    sd = stanDev(vals, avg)
    return (summed, avg, sd)


def stanDev(vals, avg):
    ar = []
    for val in vals:
        el = (val-avg)**2
        ar.append(el)
    x = sum(ar)/(len(vals)-1)
    return math.sqrt(x)


def main():
    for path in sys.argv[1:]:
        vals = summary(path)
        helpPrint(vals, path)
    pass


def helpPrint(vals, path):
    print('File:', path, 'Sum:', format(
        vals[0], '.6f'), 'Average:', format(vals[1], '.6f'), 'Stddev:', format(vals[2], '.6f'))


if __name__ == "__main__":
    main()
