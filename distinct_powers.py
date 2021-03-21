def distinctPowers(limits):
    baseLimits, exponentLimits = limits.values()

    distinctValues = set()

    for base in range(baseLimits[0], baseLimits[1]+1):
        for exponent in range(exponentLimits[0], exponentLimits[1]+1):
            distinctValues.update([base ** exponent])

    return len(distinctValues)


print(distinctPowers({"baseLimits": [2, 100], "exponentLimits": [2, 100]}))
