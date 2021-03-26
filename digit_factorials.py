from math import factorial


def getDigitFactorials():
    sumOfDigitFactorials = 0
    for number in range(10, factorial(9)):
        factorialSum = sum([factorial(int(num)) for num in str(number)])
        if factorialSum == number:
            sumOfDigitFactorials += number

    return sumOfDigitFactorials


print(getDigitFactorials())
