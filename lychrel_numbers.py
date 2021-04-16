def isPalindrome(number):
    return list(str(number)) == list(reversed(str(number)))


def isLychrel(number):
    'A number that never forms a palindrome through the reverse and add process'
    iterationCount = 0
    loopLimit = len(str(number))
    iteratedNumber = number
    localSliceIndex = -1

    while iterationCount < loopLimit:
        iteratedNumber = list(str(iteratedNumber))
        # concernedNumber = iteratedNumber
        sliceToEnd = iteratedNumber[localSliceIndex:]
        startToSlice = iteratedNumber[:localSliceIndex - 1]
        iteratedNumber = int(
            "".join(startToSlice + [concernedNumber] + sliceToEnd))

        localSliceIndex -= 1

        if abs(localSliceIndex) > len(str(iteratedNumber)):
            localSliceIndex = -1

        print(iteratedNumber)
        if isPalindrome(number + iteratedNumber):
            return False
        iterationCount += 1

    return True


print(isLychrel(349))
'''
349

394
934
943
493
439
349

move the current mobile number if it's index != 0
when the current mobile number's index becomes 0, reassign current mobile number to the number at the last index
'''


def lychrelNumbers(limit):
    return len([number for number in range(10, limit+1) if isLychrel(number)])


# print(lychrelNumbers(int(1e4)))
