def smallestMultipleOf1to20():
    smallestMultiple = 2520

    while True:
        if smallestMultiple % 1 == 0 and smallestMultiple % 2 == 0 and smallestMultiple % 3 == 0 and smallestMultiple % 4 == 0 and smallestMultiple % 5 == 0 and smallestMultiple % 6 == 0 and smallestMultiple % 7 == 0 and smallestMultiple % 8 == 0 and smallestMultiple % 9 == 0 and smallestMultiple % 10 == 0 and smallestMultiple % 11 == 0 and smallestMultiple % 12 == 0 and smallestMultiple % 13 == 0 and smallestMultiple % 14 == 0 and smallestMultiple % 15 == 0 and smallestMultiple % 16 == 0 and smallestMultiple % 17 == 0 and smallestMultiple % 18 == 0 and smallestMultiple % 19 == 0 and smallestMultiple % 20 == 0:
            return smallestMultiple
        else:
            smallestMultiple += 1


print(smallestMultipleOf1to20())
