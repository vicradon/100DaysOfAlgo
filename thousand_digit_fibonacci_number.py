def getFibDigitLength(limit):
    fib_seq = [1, 1]
    digitLength = 1

    while digitLength < limit:
        next_elem = fib_seq[-2] + fib_seq[-1]
        fib_seq.append(next_elem)
        digitLength = len(str(next_elem))

    return fib_seq.index(fib_seq[-1])+1


print(getFibDigitLength(1000))
