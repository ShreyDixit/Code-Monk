from functools import partial
import sys

N = int(input())

arr = input().split()


def func(val, i):
    n = len(val)
    start = n - 5 * (i + 1)
    if start < 0:
        if start < -4:
            return "00000"
        return ("0" * (-start)) + val[: start + 5]
    return val[start : start + 5]


def checkSorted(arr, keyFunc):
    for val in arr:
        if keyFunc(val) != "00000":
            return False
    return True


i = 0
keyFunc = partial(func, i=i)

while not checkSorted(arr, keyFunc):
    arr.sort(key=keyFunc)
    sys.stdout.write(" ".join(map(str, arr)) + "\n")
    i += 1
    keyFunc = partial(func, i=i)
