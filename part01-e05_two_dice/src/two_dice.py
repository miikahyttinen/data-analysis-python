#!/usr/bin/env python3

def main():
    for i in range(7):
        if i == 0:
            continue
        for j in range(7):
            if j == 0:
                continue
            if i+j == 5:
                print("(", i, ",", j, ")", sep="")


if __name__ == "__main__":
    main()
