from math import factorial
from functools import reduce


def factorialDigitSum(number):
    numList = list(str(factorial(number)))
    return reduce(lambda num1, num2: int(num1) + int(num2), numList)


print(factorialDigitSum(100))
