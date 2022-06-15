def main():
    x = 20
    print(f"main() x value: {x}")
    print(f"main() x id: {id(x)}")
    f1(x)


def f1(n):
    x = n
    x = 20
    print(f"f1() x value: {x}")
    print(f"f1() x id: {id(x)}")


if __name__ == '__main__':
    main()
