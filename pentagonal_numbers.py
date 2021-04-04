def minPentagonalNumbers():
    pentagonalNumbers = []

    for num in range(1, 1000):
        pentagonalNumber = int(num * (3*num - 1) * 0.5)
        pentagonalNumbers.append(pentagonalNumber)

    for index in range(1, len(pentagonalNumbers)):
        for jindex in range(index+1, len(pentagonalNumbers)):
            if pentagonalNumbers[index] + pentagonalNumbers[jindex] in pentagonalNumbers and pentagonalNumbers[jindex] - pentagonalNumbers[index] in pentagonalNumbers:
                return [index, jindex]

    return ['increase limit']


print(minPentagonalNumbers())
