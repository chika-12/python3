#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 65 and ord(x) <= 90:
        print("{}".format(x), end="")
    print()
