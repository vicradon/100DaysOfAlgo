def sumOfSquareDifference():
    sum_of_individual_squares = 0
    series_of_natural_numbers = 0
    for num in range(1, 101):
        sum_of_individual_squares += num*num
        series_of_natural_numbers += num

    square_of_series = series_of_natural_numbers * series_of_natural_numbers
    return square_of_series - sum_of_individual_squares


print(sumOfSquareDifference())
