from math import sqrt


def removeMultiples(number, arr):
    newArr = []
    for num in arr:
        if number % num != 0:
            newArr.append(num)
    newArr.append(number)

    return newArr


def sieveOfErasthothenes(limit):
    primeSet = list(range(2, limit+1))
    currentIndex = 0

    while currentIndex < len(primeSet):
        currentNum = primeSet[currentIndex]
        primeSet = primeSet[0:currentIndex+1] + \
            [num for num in primeSet[currentIndex:] if num % currentNum != 0]

        currentIndex += 1

    return len(primeSet)


def sieveOfErasthothenesWikipedia(limit):
    A = [True for i in range(2, limit+1)]

    def boolArrToArr(boolArr):
        arr = []
        for index, boolean in enumerate(boolArr):
            if boolean:
                arr.append(index + 2)
        return arr

    for i in range(2, int(sqrt(limit))):
        if A[i-2]:
            j = 0
            localCompute = int(i**2 + j*i)
            while localCompute <= limit:
                A[localCompute - 2] = False
                j += 1
                localCompute = i**2 + j*i

    return boolArrToArr(A)


def writeOutputToFile(output):
    with open('totient_maximum.txt', 'w') as fileAddr:
        fileAddr.write("n | Relative Prime" + "\n" + "\n".join(output))


def relativePrimeCount(number):
    count = 0
    tempStore = []

    for num in range(1, number):
        if gcd(num, number) == 1:
            tempStore.append(num)
            count += 1

    output.append(str(number) + " | " + ", ".join([str(i) for i in tempStore]))
    return count


def totientNumber(number, primes):
    concernedPrimes = []

    for prime in primes:
        if prime < number:
            if number % prime == 0:
                concernedPrimes.append(prime)
        else:
            break

    product = number

    for prime in concernedPrimes:
        product *= (1 - 1/prime)

    return int(product)


def totientMaximum(limit):
    numberWithHighestRatio = 0
    totientRatio = 0

    for number in range(1, limit + 1):
        newTotientRatio = number/alternateTotientFunction(number)
        if newTotientRatio > totientRatio:
            totientRatio = newTotientRatio
            numberWithHighestRatio = number

    return numberWithHighestRatio


def alternateTotientFunction(number):
    primeFactors = set(getPrimeFactors(number))

    product = number

    for prime in primeFactors:
        product *= (1 - 1/prime)

    return int(product)


# print(totientMaximum(int(1e5)))

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


primeFactors = []
primeFactorMap = {2: [2], 3: [3]}
for num in range(int(1e6)):
    if num % 2 == 0:
        primeFactorMap[2] =


print(primeFactors)
