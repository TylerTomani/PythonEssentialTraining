# def f1():
#     print("This is f1()")
# x = f1
# x()

# //
# def f1():
#     def f2():
#         print("This is f2()")
#     return f2


# x = f1()
# x()

# //
def f1(f):
    def f2():
        print("before function call")
        f()
        print("after function call")
    return f2


def f3():
    print("this is f3()")


x = f1(f3)
x()
