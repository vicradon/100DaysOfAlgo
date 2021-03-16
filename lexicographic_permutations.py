from itertools import permutations


bigNumPermutation = list(permutations('0123456789'))
millionthPermutation = bigNumPermutation[int(1e6)-1]
print("".join(millionthPermutation))
