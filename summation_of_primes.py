import math


def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True


def eliminateMultiples(num, arr):
    output = []
    for index, value in enumerate(arr):
        if value > num and value % num == 0:
            continue
        else:
            output.append(value)
    return output


def summationOfPrimes(limit=int(2e6)):
    numbersBelow2Million = list(range(2, limit))
    primesBelowRoot2Million = [num for num in range(
        int(math.sqrt(limit))+1) if isPrime(num)]

    for prime in primesBelowRoot2Million:
        regenerated_list = eliminateMultiples(prime, numbersBelow2Million)
        numbersBelow2Million = regenerated_list

    return sum(numbersBelow2Million)


print(summationOfPrimes())
