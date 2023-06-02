# context manager
with open("text.txt", "w") as f:
    f.write("Hello World")

# Manual
f = open("tst.txt", "w")
...
f.close()  # Easy to forget + Exception?
