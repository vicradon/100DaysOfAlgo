from functools import reduce


def powerDigitSum(power):
    number = 2 ** power
    return reduce(lambda num1, num2: int(num1) + int(num2), list(str(number)))


print(powerDigitSum(1000))
