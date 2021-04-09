from math import sqrt
import itertools


def isPrime(number):
    if number < 2:
        return False

    for index in range(2, int(sqrt(number) + 1)):
        if number % index == 0:
            return False

    return True


def getPermutations(number):
    permutations = itertools.permutations(str(number))
    return [int("".join(permutation)) for permutation in permutations]


def primesOfPermutation(number):
    permutations = getPermutations(number)
    primes = []

    for number in permutations:
        if isPrime(number) and len(str(number)) == 4:
            primes.append(number)

    return primes


def numbersAreASequence(numbers):
    increment = numbers[1] - numbers[0]
    for index, number in enumerate(numbers):
        if index+1 < len(numbers) and numbers[index+1] - number != increment:
            return False
    return True


def getDepth3Sequence(numbers):
    sequenceMap = {}
    combinations = []
    for index, number in enumerate(numbers):
        sequenceMap[number] = numbers[index+1:]

    for key, sequence in sequenceMap.items():
        for ind, num in enumerate(sequence):
            for index in range(len(sequence)):
                try:
                    combinations.append([key, num, sequenceMap[num][index]])
                except IndexError:
                    pass

    return combinations


def primePermutations():
    targetSequences = []
    for number in range(int(1e3), int(1e4)):
        primes = primesOfPermutation(number)

        for seq in getDepth3Sequence(primes):
            if numbersAreASequence(seq):
                strigified = "".join([str(num) for num in seq])
                targetSequences.append(strigified)

    return int(sorted(set(targetSequences))[1])


print(primePermutations())
