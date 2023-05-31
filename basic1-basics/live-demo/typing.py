a = 1

print(type(a))


print(f"Type conversion: {type(float(a))}")
print(f"Cast to string: {type(str(a))}")


# Error, notice the ","
b = "20,0"
print(f"convert to string: {type(float(b))}")
