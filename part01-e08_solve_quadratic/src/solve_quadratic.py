#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    first = b**2
    print(first)
    second = 4*a*c
    print(second)
    s = math.sqrt(first - second)
    print(s)
    print((-b + s)/2*a)
    x_1 = (-b + math.sqrt(first-second))/(2*a)
    x_2 = (-b - math.sqrt(first-second))/(2*a)
    return (x_1, x_2)


def main():
    print(solve_quadratic(4.917072, 8.620849, 0.884088))


if __name__ == "__main__":
    main()
