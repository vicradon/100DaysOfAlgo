def findLeftIndex(index, arr):
    targetNum = arr[index]
    workingArr = arr[0:index][::-1]

    for iterIndex, num in enumerate(workingArr):
        if num//targetNum == 0:
            return index - iterIndex

    return 0


def findRightIndex(index, arr):
    targetNum = arr[index]
    workingArr = arr[index+1:]

    for iterIndex, num in enumerate(workingArr):
        if num//targetNum == 0:
            return index + iterIndex

    return len(arr) - 1


def getOutreachingIndices(index, arr):
    leftIndex = index
    rightIndex = index

    leftIndex = findLeftIndex(index, arr)
    rightIndex = findRightIndex(index, arr)

    return (leftIndex, rightIndex)


def maximum_rectangle(histogram):
    store = []
    maxIndices = (0, 0)
    maxArea = 0

    if len(histogram) == 1:
        return (0, 0)

    for index, num in enumerate(histogram):
        left,  right = getOutreachingIndices(index, histogram)
        area = num * (right - left + 1)
        store.append([area, (left, right)])
        if area > maxArea:
            maxArea = area
            maxIndices = (left, right)

    return maxIndices


print(maximum_rectangle([2, 4, 2, 1, 10, 6, 10]))  # 4, 6
print(maximum_rectangle([6, 2, 5, 4, 5, 1, 6]))  # 2, 4


# currentLeft = index if index == 0 else index - 1
# currentRight = len(arr) - 1 if index == len(arr) - 1 else index + 1

# while currentLeft > 0:
#     if arr[currentLeft] // arr[index] > 0:
#         currentLeft -= 1
#     else:
#         currentLeft += 1
#         break

# while currentRight < len(arr):
#     if arr[currentRight] // arr[index] > 0:
#         currentRight += 1
#         if currentRight == len(arr):
#             currentRight -= 1
#             break
#     else:
#         currentRight -= 1
#         break


# # handle leftmost edge case
# if index == len(arr) - 1:
#     rightIndex = findRightIndex(index, arr)
#     return (leftIndex, rightIndex)

# # hangle rightmost edge case
# if index == 0:
#     leftIndex = findLeftIndex(index, arr)
#     return (leftIndex, rightIndex)
