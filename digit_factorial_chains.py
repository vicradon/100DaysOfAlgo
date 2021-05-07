from math import factorial

cache = {}


def factorialSum(number):
    return sum([factorial(int(num)) for num in str(number)])


print(factorialSum(169))


def countRepeatingTerms(number):
    encountered_numbers = [number]

    if number in cache:
        return cache[number]

    while True:
        next_number = factorialSum(encountered_numbers[-1])
        if next_number in encountered_numbers:
            cache[number] = encountered_numbers
            return encountered_numbers
        else:
            encountered_numbers.append(next_number)


def digitFactorialChains():
    count = 0

    for number in range(int(1e3), int(1e6) + 1):
        if countRepeatingTerms(number) == 60:
            count += 1

    return count


# print(digitFactorialChains())
