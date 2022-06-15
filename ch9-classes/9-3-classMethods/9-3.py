

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if "type" in kwargs else "Rooster"
        self._name = kwargs['name'] if "name" in kwargs else "Larry"
        self._sound = kwargs['sound'] if "sound" in kwargs else "Coo coo"

    def type(self, t=None):
        if t:
            self._type = t
        return self._type

    def name(self, n=None):
        if n:
            self._name = n
        return self._name

    def sound(self, s=None):
        if s:
            self._sound = s
        return self._sound

    def __str__(self):
        return(f"The {self._type} named {self._name} makes a {self._sound} noise")


def main():
    a0 = Animal(type="Dog", name="Skippy", sound="Woof woof")
    a1 = Animal()
    print(a0)
    print(a1)
    a1.sound("Quack")
    print(a1)


if __name__ == '__main__':
    main()
