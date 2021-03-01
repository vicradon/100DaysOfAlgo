import math


def specialPythagoreanTriplet():
    first_thousand_squares = [num*num for num in range(1, 1001)]
    first_thousand_numbers = range(1, 1001)

    for num_index in range(1, 1001):
        for num_offset in range(num_index+1, 1001):
            difference = 1000 - num_index - num_offset
            num_index_squared = int(math.pow(num_index, 2))
            num_offset_squared = int(math.pow(num_offset, 2))
            if num_index_squared + num_offset_squared == math.pow(difference, 2):
                return math.prod([num_index, num_offset, difference])


print(specialPythagoreanTriplet())
