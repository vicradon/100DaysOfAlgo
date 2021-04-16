import math


def combinatoricSelection():
    combinationsCount = 0
    for numerator in range(1, 101):
        for denominator in range(1, numerator+1):
            if math.comb(numerator, denominator) > 1e6:
                combinationsCount += 1
    return combinationsCount


print(combinatoricSelection())
