def main():
    list1 = ["apple", "orange", "paper", "scissors", "rock", "bananas"]
    print(list1[1:3])
    print(list1[1:6:2])
    print(list1.index("paper"))

    print("\\:".join(list1))
    printfunc(list1)


def printfunc(l):
    for i in l:
        print(i, end="::::", flush=True)


if __name__ == '__main__':
    main()
