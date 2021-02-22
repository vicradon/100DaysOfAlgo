from functools import reduce


def sumOfEvenFibonacciNumbers():
    sequence = [1, 2]
    while sequence[-1] < 4000000:
        sum_of_last_two = sequence[-1] + sequence[-2]

        if sum_of_last_two > 4000000:
            break

        sequence.append(sum_of_last_two)

    even_nums_in_seq = filter(lambda num: num % 2 == 0, sequence)
    return reduce(lambda num1, num2: num1+num2, even_nums_in_seq)


print(sumOfEvenFibonacciNumbers())
