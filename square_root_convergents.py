from fractions import Fraction
import sys
sys.setrecursionlimit(1500)


def seq(iterationLimit, iterationCount=0):
    if iterationCount == iterationLimit:
        return 0

    iterationCount += 1
    return 1/(2 + seq(iterationLimit, iterationCount))


def squareRootConvergentsRecursive():
    numeratorMoreThanDenominatorCount = 0
    arr = []

    for index in range(1001):
        iterationValue = 1 + Fraction(seq(index)).limit_denominator()
        if len(str(iterationValue.numerator)) > len(str(iterationValue.denominator)):
            print(index)
            numeratorMoreThanDenominatorCount += 1
            arr.append(iterationValue)

    print(arr)
    return numeratorMoreThanDenominatorCount


def squareRootConvergentsIterative():
    numeratorMoreThanDenominatorCount = 0

    fraction = 1 + Fraction(1, 2)

    for index in range(1000):
        numerator = fraction.numerator + (2 * fraction.denominator)
        denominator = fraction.numerator + fraction.denominator

        fraction = Fraction(numerator, denominator)

        if len(str(fraction.numerator)) > len(str(fraction.denominator)):
            numeratorMoreThanDenominatorCount += 1

    return numeratorMoreThanDenominatorCount


print(squareRootConvergentsIterative())
