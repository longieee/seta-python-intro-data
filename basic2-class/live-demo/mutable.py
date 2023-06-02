a = list(range(10))  # 0 1 ... 9


# Pass by referece!
def playlist(a: list):
    for i in range(len(a)):
        a[i] += 1


playlist(a)
print(a)  # ?
