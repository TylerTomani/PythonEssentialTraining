# In chapter 8. Lesson 6 - Mixed structures, is anyone having problems with
#  the global variable dlevel? When I declare in the disp() func as global dlevel

def main():
    r = range(11)
    l = [1, 'two', 3, {4: 'four'}, 5]
    t = ('one', 'two', None, 'four', 'five')
    s = set("It's a bird! it's a plane! It's Superman!")
    d = dict(one=r, two=l, three=s)
    mixed = [l, r, s, d, t]
    disp(mixed)


def disp(o):
    global dlevel
    # dlevel = 0

    dlevel += 1
    if isinstance(o, list):
        print_list(o)
    elif isinstance(o, range):
        print_list(o)
    dlevel -= 1

    if dlevel <= 1:
        print()


def print_list(o):
    print('[', end=' ')
    for x in o:
        disp(x)
    print(']', end=' ', flush=True)


if __name__ == '__main__':
    main()
