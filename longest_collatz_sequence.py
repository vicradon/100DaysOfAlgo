def longestCollatzSequence(limit):
    collatz_mapping = {}
    for index in range(limit):
        collatz_seq = [limit - index]

        last_elem = collatz_seq[-1]
        while last_elem != 1:
            if last_elem % 2 == 0:
                collatz_seq.append(last_elem//2)
            else:
                collatz_seq.append((3 * last_elem) + 1)
            last_elem = collatz_seq[-1]

        collatz_mapping[limit - index] = len(collatz_seq)

    return max(collatz_mapping, key=collatz_mapping.get)


print(longestCollatzSequence(int(1e6)))
