# Mutable
a = [1, 2, 3, 4]

# Immutable
b = (1, 2, 3, 4)

a[1] = 5
# b[1] = 5

print(a)
print(b)  # Error


for i in a:
    print(i)
