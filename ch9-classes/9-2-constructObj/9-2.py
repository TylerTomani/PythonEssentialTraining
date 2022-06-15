class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else "Rooster"
        self._name = kwargs['name'] if 'name' in kwargs else "Fuzzy"
        self._sound = kwargs['sound'] if 'sound' in kwargs else "coo coo"

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError("print_animal(): must be type Animal")
    else:
        print("The {} dog name {} makes a {} sound".format(
            o._type, o._name, o._sound))


def main():
    a0 = Animal(type="Cat", name="Mitten", sound="meow")
    a1 = Animal(type="Dog", name="Rooster", sound="woof")
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type="Cow", name="Suzie", sound="moo"))
    print_animal(Animal())


if __name__ == '__main__':
    main()
