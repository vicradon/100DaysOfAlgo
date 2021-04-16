def sameDigits(numbers):
    sortedNumbers = [sorted(str(number)) for number in numbers]
    firstSortedNumber = sortedNumbers[0]

    for number in sortedNumbers:
        if number != firstSortedNumber:
            return False

    return True


def permutedMultiples(limit):
    currentNumber = 1
    while True:
        currentNumberMultiples = [
            currentNumber * i for i in range(1, limit + 1)]
        if sameDigits(currentNumberMultiples):
            return currentNumber
        else:
            currentNumber += 1


print(permutedMultiples(6))
