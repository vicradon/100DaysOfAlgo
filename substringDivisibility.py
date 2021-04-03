from itertools import permutations


def isSubstringDivisible(number):
    strigified_number = str(number)

    def remainderExists(limits, divisor):
        return int(strigified_number[limits[0]-1:limits[1]]) % divisor != 0

    conditions = [([2, 4], 2), ([3, 5], 3), ([4, 6], 5),
                  ([5, 7], 7), ([6, 8], 11), ([7, 9], 13), ([8, 10], 17)]

    for condition in conditions:
        if remainderExists(condition[0], condition[1]):
            return False

    return True


def isPandigital(number):
    numberAsSet = set(str(number))
    pandigitalSet = set('0123456789')

    return numberAsSet == pandigitalSet


def main():
    targetSum = 0
    pandigitals = [int("".join(num))
                   for num in list(permutations('0123456789'))]
    # pandigitalPermutations = list(permutations('0123456789'))

    for number in pandigitals:
        if isSubstringDivisible(number):
            targetSum += number

    return targetSum


print(main())
