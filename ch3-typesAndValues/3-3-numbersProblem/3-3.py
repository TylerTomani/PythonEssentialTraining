from decimal import *
from unicodedata import decimal
# x = 7 / 3
# print(x)
# print(type(x))

x = .1 + .1 + .1 - .3
print(x)
print(type(x))

a = Decimal(".10")
b = Decimal(".30")
x = a + a + a - b
print(x)
print(type(x))
