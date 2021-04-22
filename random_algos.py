def lastDigitMovement(num):
    "The last digit is moved for all possible permutations"
    modifiedNum = list(str(num))
    currentIndex = -1

    for i in range(factorial(len(str(num)))):
        nextIndex = currentIndex - 1
        itemAtNextIndex = modifiedNum[nextIndex]
        itemAtCurrentIndex = modifiedNum[currentIndex]

        modifiedNum[nextIndex] = itemAtCurrentIndex
        modifiedNum[currentIndex] = itemAtNextIndex

        print(num + int("".join(modifiedNum)))
        if isPalindrome(num + int("".join(modifiedNum))):
            return True

        if abs(nextIndex) == len(modifiedNum):
            currentIndex = -1
        else:
            currentIndex -= 1

    return False
