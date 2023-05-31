a = [i for i in range(10)]

for i in range(10):
    print(i)


d = {"a": 1, "b": 2, "c": 3}

# d.items()
# d.keys()
# d.values()
# Always return in order of original dictionary
# will not sort for you!
x = [k for k, v in d.items()]

# print(a)
# print(x)


# Nested list interpretation
nested = [i + j for j in list(range(10)) for i in list(range(100, 110))]

print(nested)
