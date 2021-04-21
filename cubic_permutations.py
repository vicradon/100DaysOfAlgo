def sortCube(number):
    return "".join(sorted(str(number)))


def cubicPermutations():
    numbersForCubicPermutations = {}  # cube, count
    currentNumber = 1

    while True:
        sortedCube = sortCube(currentNumber ** 3)
        try:
            numbersForCubicPermutations[sortedCube] = numbersForCubicPermutations[sortedCube] + [
                currentNumber]
        except KeyError:
            numbersForCubicPermutations[sortedCube] = [currentNumber]

        if len(numbersForCubicPermutations[sortedCube]) == 5:
            return numbersForCubicPermutations[sortedCube][0] ** 3

        currentNumber += 1


print(cubicPermutations())
