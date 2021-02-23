import math


def largestPrimeFactor(number):
    prime_factors = []

    while number % 2 == 0:
        prime_factors.append(2)
        number = number / 2

    for num in range(3, int(math.sqrt(number)) + 1, 2):
        while number % num == 0:
            prime_factors.append(num)
            number = number / num

    if number > 2:
        prime_factors.append(number)

    return max(prime_factors)


print(largestPrimeFactor(600851475143))

# Explanation
# This algorithm first finds all the prime factors of the given number.
# It does this by reducing the number if even to odd.
# Then, it runs a for loop from 3 to the square root of the number.
# The number is progressively reduced by dividing by the previous number.

# Finally, it the number wasn't in the sqrt range, we add it to primes as
# it is prime.
