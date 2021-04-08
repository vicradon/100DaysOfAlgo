from math import sqrt


def getPrimeFactors(number):
    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for num in range(3, int(sqrt(number)) + 1, 2):
        while number % num == 0:
            prime_factors.append(num)
            number = number / num

    if number > 2:
        prime_factors.append(int(number))

    return prime_factors


def combineSimilar(group):
    hashMap = {}
    output = []
    for num in group:
        try:
            hashMap[num] = hashMap[num] + 1
        except KeyError:
            hashMap[num] = 1

    for key in hashMap:
        output.append(key*hashMap[key])
    return output


def setsAreDistinctAndSameLength(sets, setLength):
    iteratedItems = []

    for index in range(len(sets)):
        if len(sets[index]) != setLength:
            return False
        for item in sets[index]:
            if item in iteratedItems:
                return False
            iteratedItems.append(item)

    return True


def firstNConsectiveDistintPrimeFactorNumbers(limit):
    currentNumber = 10
    consecutiveNumbers = []
    primeFactorSets = []

    while True:
        consecutiveNumbers = [currentNumber + index for index in range(limit)]
        primeFactorSets = [combineSimilar(getPrimeFactors(number))
                           for number in consecutiveNumbers]

        if setsAreDistinctAndSameLength(primeFactorSets, limit):
            break

        currentNumber += 1

    return consecutiveNumbers[0]


print(firstNConsectiveDistintPrimeFactorNumbers(4))
