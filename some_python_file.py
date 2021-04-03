def someFunc(arg1, arg2):
    arg1 = arg2
    print(arg1)


def main():
    int1 = 4
    int2 = 8

    print(int1)
    someFunc(int1, int2)
    print(int1)


main()
