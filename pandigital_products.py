def isPandigital(multiplier, multiplicand, limit=9):
    fullSet = list(range(1, limit+1))
    formedStringSet = str(multiplier) + str(multiplicand) + \
        str(multiplier * multiplicand)
    formedSet = sorted([int(num) for num in formedStringSet])

    return fullSet == formedSet


def pandigitalProducts(limit):
    pandigitalProducts = set()
    for index1 in range(1, limit):
        for index2 in range(index1, limit):
            if (isPandigital(index1, index2)):
                pandigitalProducts.update([index1 * index2])

    return sum(pandigitalProducts)


print(pandigitalProducts(int(1e4)))
