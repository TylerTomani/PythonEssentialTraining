def main():
    r = int(input("Enter range: "))
    # for i in range(int(r)):
    #     print(f"{i}", end=" ")

    for i in inclusive_range(r):
        print(i, end=" ")
    print()


def inclusive_range(*args):
    numargs = len(args)
    start = 0
    step = 1
# // initlialize parameters
    if numargs < 1:
        raise TypeError("Not enough arguments: 1-3")
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args  # will format so 2nd parameter is stop
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("too many arguments: 1-3")
# // Generator
    i = start
    while i <= stop:
        yield 1
        i += step


if __name__ == '__main__':
    main()
