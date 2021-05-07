import math


def numberOfFactors(number):
    factors = {1, number}
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            factors.update((i, number//i))
    return len(factors)


def triangleNumberWithOverNFactors(factorCount):
    currentTriangleNumber = 1
    currentNaturalNumber = 2
    while True:
        currentTriangleNumber += currentNaturalNumber
        currentNaturalNumber += 1

        if numberOfFactors(currentTriangleNumber) > factorCount:
            return currentTriangleNumber


print(triangleNumberWithOverNFactors(500))
