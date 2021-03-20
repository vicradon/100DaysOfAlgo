def numberSpiralDiagonals(gridSide):
    startCount = 2
    startDiagonal = 1

    if gridSide % 2 == 0:
        startCount = 1
        startDiagonal = 0

    diagonals = [startDiagonal]

    count = startCount
    while diagonals[-1] < gridSide*gridSide:
        for i in range(4):
            diagonals.append(diagonals[-1] + count)
        count += 2

    return sum(diagonals)


print(numberSpiralDiagonals(1001))
