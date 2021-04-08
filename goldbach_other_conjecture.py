from math import sqrt, pow


def isPrime(number):
    if number < 2:
        return False

    for index in range(2, int(sqrt(number) + 1)):
        if number % index == 0:
            return False

    return True


def getNextOddComposite(composite):
    aggregate = composite + 2
    while True:
        if not(isPrime(aggregate)) and aggregate % 2 != 0:
            return aggregate
        else:
            aggregate += 2


def getNextDoubledsquare(currentDoubledsquare):
    baseNum = sqrt(currentDoubledsquare//2)
    return 2 * int(pow(baseNum + 1, 2))


def satisfiesGoldbachConjecture(number):
    currentDoubledSquare = 2

    while not(isPrime(number - currentDoubledSquare)):
        currentDoubledSquare = getNextDoubledsquare(currentDoubledSquare)

        if currentDoubledSquare > number:
            return False

    return True


def smallestNonGoldbachOddComposite():
    currentComposite = 33
    while satisfiesGoldbachConjecture(currentComposite):
        currentComposite = getNextOddComposite(currentComposite)

    return currentComposite


print(smallestNonGoldbachOddComposite())
