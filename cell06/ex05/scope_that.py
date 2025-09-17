def add_one(n):
    n = n + 1
    print("Inside function, n =", n)

x = 42
print("Before function call, x =", x)

add_one(x)

print("After function call, x =", x)