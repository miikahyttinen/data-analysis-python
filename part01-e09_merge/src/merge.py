#!/usr/bin/env python3

import numpy as np


def merge(l1, l2):
    L1 = list(l1)
    L2 = list(l2)
    c = len(L1) + len(L2)
    l = []
    while len(l) < c:
        if (len(L2) != 0) and (len(L1) != 0):
            if L1[0] < L2[0]:
                l.append(L1.pop(0))
            else:
                l.append(L2.pop(0))
        else:
            break
    if len(L1) > 0:
        l = l + L1
    if len(L2) > 0:
        l = l + L2
    return l


def main():
    list_1 = [1, 2, 5]
    list_2 = [4, 7, 9]
    m = merge(list_1, list_2)
    print(list_1)
    print(list_2)
    pass


if __name__ == "__main__":
    main()
