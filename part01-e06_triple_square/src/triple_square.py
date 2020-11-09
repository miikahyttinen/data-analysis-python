#!/usr/bin/env python3


def main():
    for i in range(11):
        if i == 0:
            continue
        tri = triple(i)
        squ = square(i)
        if tri < squ:
            break
        print("triple(", i, ")==", tri, " ",
              "square(", i, ")==", squ, sep="")


def triple(num):
    return num*3


def square(num):
    return pow(num, 2)


if __name__ == "__main__":
    main()
