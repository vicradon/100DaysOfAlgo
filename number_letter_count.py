def wordFromNumber(num):
    units = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    firstTens = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }

    remainingTensStarters = {
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
    }

    hundredsStarters = {
        100: 'one hundred',
        200: 'two hundred',
        300: 'three hundred',
        400: 'four hundred',
        500: 'five hundred',
        600: 'six hundred',
        700: 'seven hundred',
        800: 'eight hundred',
        900: 'nine hundred',
    }

    if num < 1 or num > 1000:
        return ""

    if num < 10:
        return units[num]

    if num >= 10 and num < 20:
        return firstTens[num]

    if num >= 20 and num < 100:
        if num in remainingTensStarters:
            return remainingTensStarters[num]

        tensPart = num//10 * 10
        unitsPart = num % 10
        return remainingTensStarters[tensPart] + "-" + units[unitsPart]

    if num >= 100 and num < 1000:
        if num in hundredsStarters:
            return hundredsStarters[num]

        hundredsPart = num//100 * 100
        tensPart = wordFromNumber(num - hundredsPart)
        return hundredsStarters[hundredsPart] + ' and ' + tensPart

    return "one thousand"


def letterCount(word):
    print(word)
    return len(list(filter(lambda char: char != " " and char != "-", list(word))))


def numberLetterCount(limit):
    return sum([letterCount(wordFromNumber(num)) for num in range(1, limit + 1)])


print(numberLetterCount(1001))
