#!/usr/bin/env python3

import math


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle):")
        if shape == '':
            break
        if shape == "triangle":
            b = input("Give base of the triangle:")
            h = input("Give heigth of the triangle:")
            print("The area is", int(b)*int(h)/2)
        if shape == "rectangle":
            b = input("Give base of the rectangle:")
            h = input("Give heigtht of the rectangle:")
            print("The area is", int(b)*int(h))
        if shape == "circle":
            r = input("Give radius of the circle:")
            print("The area is", pow(int(r), 2)*math.pi)
        if not(shape) in ["circle", "triangle", "rectangle"]:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
