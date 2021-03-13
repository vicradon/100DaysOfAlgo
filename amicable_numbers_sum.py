import math


def factorSum(num):
    factors = {1}

    for index in range(2, int(math.sqrt(num)) + 1):
        if num % index == 0:
            factors.update((index, num//index))

    return sum(factors)


def amicableNumbersSum(limit):
    numberFactorSums = {}

    for index in range(1, limit):
        numberFactorSums[index] = factorSum(index)

    amicableNumbers = set()
    for key, value in numberFactorSums.items():
        if value in numberFactorSums and numberFactorSums[value] == key and key != value:
            amicableNumbers.update((key, value))

    return sum(amicableNumbers)


print(amicableNumbersSum(10000))
