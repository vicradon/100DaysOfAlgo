from functools import reduce


def sumOfMultiplesOf3And5(rangeMin, rangeMax):
    if rangeMin <= 0:
        return "rangeMin must be greater than 0"

    multiples = []
    for num in range(rangeMin, rangeMax):
        if num % 3 == 0 and num % 5 == 0:
            multiples.append(num)
            continue
        if num % 3 == 0:
            multiples.append(num)
            continue
        if num % 5 == 0:
            multiples.append(num)
            continue

    return reduce(lambda num1, num2: num1+num2, multiples)


print(sumOfMultiplesOf3And5(1, 1000))
