# x = [1, 2, 3, 4, 5]
# x[2] = 97
# for i in x:
#     print(f"i : {i}")

# x = (1, 2, 3, 4, 5)
# for i in x:
#     print(f"i : {i}")

# x = range(4)
# for i in x:
#     print(f"i: {i}")

# x = range(5, 50, 5)
# for i in x:
#     print(f"i: {i}", end=" ", flush=True)

x = list(range(4))
x[1] = 99
for i in x:
    print(f"i: {i}")

dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
dict['four'] = 99
for k, v in dict.items():
    print("key: {} value: {}".format(k, v))
