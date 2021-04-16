from math import sqrt


def isPrime(number):
    if number < 2:
        return False

    for index in range(2, int(sqrt(number) + 1)):
        if number % index == 0:
            return False

    return True


def sieveOfErasthosenes(limit):
    return [number for number in range(limit) if isPrime(number)]

# Find a way to sum sub primes to a particular prime
# have a map that extends to 1e6 and has the sub prime length as values


def numberOfSubPrimes(primes):
    startingPos = 0
    endPoint = 1

    while endPoint < len(primes):
        cumulative = sum(primes[startingPos:endPoint])


def getPrimeSequenceLength(prime, primesBelowLimit):
    primeSubset = primesBelowLimit[0:primesBelowLimit.index(prime)+1]
    startingIndex = 0
    endingIndex = 1
    subSum = sum(primeSubset[startingIndex:endingIndex])

    while True:
        while subSum < prime:
            endingIndex += 1
        if subSum == prime:
            return "yah!"
        startingIndex += 1
        endingIndex += startingIndex + 1
        return subSum


def consecutivePrimeSum(limit):
    primesBelowLimit = sieveOfErasthosenes(limit)
    subPrimesCount = {}
    for num in primesBelowLimit:
        subPrimesCount[num] = getPrimeSequenceLength(num, primesBelowLimit)
    return subPrimesCount


print(consecutivePrimeSum(5))
