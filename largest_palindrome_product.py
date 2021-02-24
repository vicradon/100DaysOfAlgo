def largestPalindromeProduct():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            string_product = str(product)
            reversed_string_product = string_product[::-1]
            if reversed_string_product == string_product:
                palindromes.append(product)

    return max(palindromes)


print(largestPalindromeProduct())
