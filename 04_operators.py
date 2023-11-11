x = 10
y = 5

print(x + y)
print(x - y)
print(x * y)
print(x / y)  # gives decimal value. 2.0
print(x // y)  # gives floor  value. 2 if 2.5
print(round(x / y))  # gives floor  value. 3 if 2.5
print(x ** y)  # gives the power of the values

# comparision operator
print(x >= y)
print(x <= y)
print(x != y)
print(x == y)
print(x < y)
print(x > y)


a = True
b = True

# boolean operator
print(not a)
print(a and b)
print(a or b)

# Let's create a if, else example

name = "paulp"

if name == "paul":
    print("prabahar")
else:
    print("not prabahar")


# Ternary Operator
print("prabahar") if name == "paul" else print("not prabahar")
