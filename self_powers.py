def selfPowers():
    seriesSum = 0
    for number in range(1, 1001):
        seriesSum += number ** number

    return str(seriesSum)[-10:]


print(selfPowers())
