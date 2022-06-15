def main():
    animals = dict(cow="moo", cat="meow", dog="wood", lion="grr")

    for i in animals:
        print(f"{animals[i]}: {i} ")

    for k, v in animals.items():
        print(f"{k} : {v}")


if __name__ == '__main__':
    main()
