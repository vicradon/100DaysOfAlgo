def isPandigital(number, concat_set):
    products = [str(number * multiplier) for multiplier in concat_set]
    return sorted("".join(products)) == list('123456789')


def largest1to9PandigitalMultiples():
    concat_sets = [list(range(1, num+1)) for num in range(1, 10)]

    pandigitals = []

    # 100000000
    for num in range(200000):
        for concat_set in concat_sets:
            if isPandigital(num, concat_set):
                pandigitals.append(num)

    return pandigitals


print(largest1to9PandigitalMultiples())
