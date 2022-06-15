def main():
    x = dict(Cow="moo", Pig="oink", Cat="meow", Dog="woof")
    animals(**x)


def animals(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print(f"key: {k} value: {kwargs[k]}")
    else:
        print("Empty")


if __name__ == '__main__':
    main()
