#!/usr/bin/env python3

import re
import os


def file_listing(filename="src/listing.txt"):
    f = open(filename, mode="r")
    lines = []
    for line in f:
        reg = re.findall(r'hyad.*', line)
        splitted = reg[0].split(' ')
        trimmed = help(splitted)
        lines.append(trimmed)
    print(lines)
    return lines


def help(arr):
    l = []
    for s in arr:
        if s != 'hyad-all' and s != '':
            if bool(re.search(':', s)):
                l.append(s.split(':')[0])
                l.append(s.split(':')[1])
            else:
                l.append(s)
    return (int(l[0]), l[1], int(l[2]), int(l[3]), int(l[4]), l[5])


def main():
    file_listing()


if __name__ == "__main__":
    main()
