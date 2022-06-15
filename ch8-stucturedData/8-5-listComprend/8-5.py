def main():
    seq = range(5)
    seq2 = [x * 2 for x in seq]
    printSeq(seq)
    print()
    printSeq(seq2)


def printSeq(s):
    for i in s:
        print(i, end=" ")


if __name__ == '__main__':
    main()
