def main():
    kitten("meow", "prr", "grr")
    kitten()


def kitten(*args):
    if len(args):
        for i in args:
            print(i)
    else:
        print("meow")


if __name__ == '__main__':
    main()
