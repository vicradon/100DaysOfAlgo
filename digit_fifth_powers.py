def sumOfPowers(number, exponent):
    return sum([int(num) ** exponent for num in str(number)])


def digitNthPowers(exponent):
    powerSum = 0

    for num in range(10**(exponent-1), exponent * (9**exponent)):
        if sumOfPowers(num, exponent) == num and num > 1:
            powerSum += num

    return powerSum


print(digitNthPowers(5))
