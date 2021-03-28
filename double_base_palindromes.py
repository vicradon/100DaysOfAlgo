def base2(num):
    return int("{0:b}".format(num))


def isPalindrome(num):
    return str(num) == str(num)[::-1]


def doubleBasePalindromes(limit):
    return sum([num for num in range(limit) if isPalindrome(num) and isPalindrome(base2(num))])


print(doubleBasePalindromes(int(1e6)))
