def sumOfMultiplesOf3or5(rangeMin, rangeMax):
    return sum([num for num in range(rangeMin, rangeMax) if num % 3 == 0 or num % 5 == 0])


print(sumOfMultiplesOf3or5(1, 1000))
