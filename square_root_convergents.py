from fractions import Fraction
import sys
sys.setrecursionlimit(1500)


def seq(iterationLimit, iterationCount=0):
    if iterationCount == iterationLimit:
        return 0

    iterationCount += 1
    return 1/(2 + seq(iterationLimit, iterationCount))


def squareRootConvergents():
    numertorMoreThanDenominatorCount = 0
    arr = []

    for index in range(1, 1002):
        iterationValue = 1 + Fraction(seq(index)).limit_denominator()
        if len(str(iterationValue.numerator)) > len(str(iterationValue.denominator)):
            numertorMoreThanDenominatorCount += 1
    return numertorMoreThanDenominatorCount


print(squareRootConvergents())
