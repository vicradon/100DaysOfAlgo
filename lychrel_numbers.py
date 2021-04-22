def isPalindrome(number):
    return list(str(number)) == list(reversed(str(number)))


def isLychrel(num):
    currentSum = num
    iterationCount = 0
    while iterationCount < 50:
        if isPalindrome(currentSum + int(str(currentSum)[::-1])):
            return False
        currentSum = currentSum + int(str(currentSum)[::-1])
        iterationCount += 1

    return True


def lychrelNumbers(limit):
    return len([number for number in range(10, limit+1) if isLychrel(number)])


print(lychrelNumbers(int(1e4)))
