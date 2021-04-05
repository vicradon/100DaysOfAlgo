from math import sqrt


def nextTriPentHexNumber():
    def computeTriangularNum(n): return n*(n + 1)*0.5

    def isPentagonal(num):
        pentComputation = (1 + sqrt(1 + 24 * num)) * (1/6)
        return pentComputation == int(pentComputation)

    def isHexagonal(num):
        hexComputation = 0.25 * (1 + sqrt(1 + 8 * num))
        return hexComputation == int(hexComputation)

    iterCount = 286

    while True:
        triangularNum = computeTriangularNum(iterCount)

        if isPentagonal(triangularNum) and isHexagonal(triangularNum):
            return int(triangularNum)

        iterCount += 1


print(nextTriPentHexNumber())
