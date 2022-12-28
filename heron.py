from math import sqrt as sr
from math import fabs as fa

def heron(n, error, prev = 1.0):
    approx = (prev + (n / prev)) / 2.0
    if (fa(sr(n) - approx) < error):
        return approx
    else:
        return heron(n, error, approx)

if __name__ == "__main__":
    print("Give a number to square root: ", end='')
    i = float(input())
    print("Give a margin of error: ", end='')
    e = float(input())
    result = heron(i, e)
    print("Approximate square root of", i, "is: ", result)