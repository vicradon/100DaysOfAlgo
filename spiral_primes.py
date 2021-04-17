from math import sqrt
from fractions import Fraction


def isPrime(number):
    if number < 2:
        return False

    for index in range(2, int(sqrt(number)) + 1):
        if number % index == 0:
            return False

    return True


def spiralPrimes():
    diagonals = [1, 3, 5, 7, 9]
    current_grid_side = 3
    primeCount = 3
    increment = 4

    while True:
        for i in range(4):
            num = diagonals[-1] + increment
            diagonals.append(num)
            if isPrime(num):
                primeCount += 1

        increment += 2
        current_grid_side += 2

        primeRatio = primeCount/len(diagonals)

        if primeRatio < 0.1:
            return current_grid_side


print(spiralPrimes())
