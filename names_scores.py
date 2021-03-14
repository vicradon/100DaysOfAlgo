def wordToInt(word):
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    return sum([alphabets.index(char) + 1 for char in word.lower()])


def nameScores(names):
    sortedNames = sorted(names)
    return sum([wordToInt(word) * (index + 1) for index, word in enumerate(sortedNames)])


namesFile = open("p022_names.txt", "r")
raw_names = namesFile.read()
names = list(filter(lambda char: char !=
                    ',' and char != '', raw_names.split('"')))

print(nameScores(names))
