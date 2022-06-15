def main():
    a = set("We're going to need a bigger string")
    b = set("sorry dave can't Do that")
    print(a)
    print(b)
    printSet(a)


def printSet(s):
    for i in s:
        print(i, end=" ", flush=True)


if __name__ == '__main__':
    main()
