from fractions import Fraction
from math import prod


def digitCancellingFractions():
    cancelling_fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator+1, 100):
            numerator_first_digit = str(numerator)[0]
            numerator_second_digit = str(numerator)[1]
            denominator_first_digit = str(denominator)[0]
            denominator_second_digit = str(denominator)[1]

            if numerator != denominator:
                try:
                    if numerator_first_digit == denominator_second_digit:
                        if int(numerator_second_digit)/int(denominator_first_digit) == numerator/denominator:
                            cancelling_fractions.append(
                                numerator/denominator)
                    if numerator_second_digit == denominator_first_digit:
                        if int(numerator_first_digit)/int(denominator_second_digit) == numerator/denominator:
                            cancelling_fractions.append(
                                numerator/denominator)

                except ZeroDivisionError:
                    pass

    fractional_product = Fraction(
        prod(cancelling_fractions)).limit_denominator()
    return fractional_product.denominator


print(digitCancellingFractions())
