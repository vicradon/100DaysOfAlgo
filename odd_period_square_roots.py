from math import sqrt, floor
from fractions import Fraction


def getPeriodOfRoot(number):
    targetNum = number
    period = 1

    startingNumber = floor(sqrt(number))
    targetNum = sqrt(number) - startingNumber

    store = [startingNumber]

    while True:
        nextWhole = floor(1/targetNum)
        store.append(nextWhole)
        targetNum = 1/targetNum - nextWhole

        if nextWhole == 36:
            return period

        if startingNumber * 2 == nextWhole:
            print(store)
            return period
        else:
            period += 1


print(getPeriodOfRoot(337))


def oddPeriodSquares(limit):
    oddPeriodSquaresCount = 0
    for num in range(2, limit + 1):
        if sqrt(num).is_integer():
            continue

        period = getPeriodOfRoot(num)
        if period % 2 != 0:
            oddPeriodSquaresCount += 1
    return oddPeriodSquaresCount


# print(oddPeriodSquares(10000))
