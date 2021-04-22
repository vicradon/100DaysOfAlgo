def powerfulDigitCounts():
    targetNumberCount = 0

    for base in range(1, 10):
        exponent = 0
        while exponent <= len(str(base ** exponent)):
            exponent += 1
            if len(str(base ** exponent)) == exponent:
                targetNumberCount += 1

    return targetNumberCount


print(powerfulDigitCounts())
