def extractTree():
    with open('p067_triangle.txt', 'r') as fileAddr:
        content = fileAddr.read()
        lines = content.split("\n")
        reversedLines = reversed(lines)

        output = []

        for line in reversedLines:
            output.append([int(char) for char in line.split(" ")])

        return output


def maxPathSum(tree):
    if len(tree) == 1:
        return tree[0][0]

    idealPaths = []
    for index in range(len(tree[0]) - 1):
        leftSum = tree[0][index] + tree[1][index]
        rightSum = tree[0][index + 1] + tree[1][index]

        if leftSum > rightSum:
            idealPaths.append(leftSum)
        else:
            idealPaths.append(rightSum)

    return maxPathSum([idealPaths] + tree[2:])


tree1 = extractTree()
print(maxPathSum(tree1))
