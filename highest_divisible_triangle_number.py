import math


def triangleNumber(index):
    return sum([i+1 for i in range(index)])


def numberOfFactors(number):
    factors = {1, number}
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            factors.update((i, number//i))
    return len(factors)

# number of factors < sqrt * 2
# we are looking for a number with over 500 factors
# so we need a number greater than the square of 500


def triangleNumberWithOverNFactors(number):
    triangleNumbers = [triangleNumber(number)
                       for number in range(number * number * 2)]
    return triangleNumbers

# number with over 500 factors will be a number = square(500)*2


# print(triangleNumberWithOverNFactors(500))
print(numberOfFactors(1e14))
