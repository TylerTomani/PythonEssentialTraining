# str = """
# The Number Seven
# """
# print(str)

# str2 = "this is a string"

# print(str2.capitalize())

# str3 = "This is lowercase".upper()
# print(str3.lower())

# nums = "The numbers {} {}".format(8, 9)
# print(nums)

x = "Two values {} {}".format(3, 7)
print(x)

x = "Two values {1} {0}".format(3, 7)
print(x)
x = 'Two values "{1:<09}" "{0:>09}"'.format(3, 7)
print(x)

x = 5
y = 9
str = f"Two Values {x} {y}"
print(str)
