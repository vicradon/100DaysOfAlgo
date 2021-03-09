import math


def latticePaths(gridSide):
    return math.comb(gridSide * 2, gridSide)


print(latticePaths(20))
