import math


def isAbundant(number):
    factors = {1}
    for index in range(2, int(math.sqrt(number)) + 1):
        if number % index == 0:
            factors.update((index, number//index))

    if sum(factors) > number:
        return True
    return False


def nonAbundantSums(num):
    limit = 28123
    abundantNumsBelowLimit = [
        num for num in range(1, limit+1) if isAbundant(num)]

    # compoundAbundantSums = set()
    # for number in range(1, limit + 1):
    #     for index in range(1, number//2 + 1):
    #         if index in abundantNumsBelowLimit and (number - index) in abundantNumsBelowLimit:
    #             compoundAbundantSums.update([number])

    # return compoundAbundantSums

    stuff = []
    for i in range(1, len(abundantNumsBelowLimit)):
        if (num - i) in abundantNumsBelowLimit and i in abundantNumsBelowLimit:
            stuff.append([i, num - i])

    return stuff


print(nonAbundantSums(28123))

# in the sum of the subtracted, if both are abundant, break the loop


# for abundantNumber in abundantNumsBelowLimit:
#     if (number - abundantNumber) in abundantNumsBelowLimit:
#         compoundAbundantSums.append(number)
