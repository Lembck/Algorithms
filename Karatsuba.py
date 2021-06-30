from math import ceil
import random

def digits(x):
    if x < 10:
        return 1
    else:
        return 1 + digits(x/10)

def split(x, half):
    s = str(x)
    if len(s) < half * 2:
        s = "0" * (2*half-len(s)) + s
    #print("Splitting " + s + " by " + str(half) + " into " + s[:half] + " and " + s[half:])
    return int(s[:half]), int(s[half:])

def Karatsuba(x, y, n = -1):
    if (n == 1):
        return x * y
    elif (n == -1):
        n = max(digits(x), digits(y))
    half = ceil(n/2)
    
    a, b = split(x, half)
    c, d = split(y, half)

    e = Karatsuba(a, c, half)
    f = Karatsuba(b, d, half)
    n_1 = b-a < 0
    n_2 = c-d < 0
    gPositive = (n_1 and n_2) or (not n_1 and not n_2)
    g = Karatsuba(abs(b-a), abs(c-d), half)
    if not gPositive:
        g *= -1
    return pow(10, 2*half) * e + pow(10, half) * (e + f + g) + f

def compareKaratsuba(x = random.randint(10, 999999), y = random.randint(10, 999999)):
    print("Karatsuba: " + str(Karatsuba(x, y)) + "\nMultiplcation: " + str(x*y))

compareKaratsuba()
