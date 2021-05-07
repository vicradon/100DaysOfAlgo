from math import sqrt


def getDoiphantineNumber(number):
    if sqrt(number).is_integer():
        return 0

    currentYValue = 1
    currentXValue = sqrt(1 + number*(currentYValue**2))

    while not(currentXValue.is_integer()):
        currentYValue += 1
        currentXValue = sqrt(1 + number*(currentYValue**2))

    return int(currentXValue)


def largestMaxValue(limit):
    return max([getDoiphantineNumber(number) for number in range(1, limit+1)])


print(largestMaxValue(1000))
