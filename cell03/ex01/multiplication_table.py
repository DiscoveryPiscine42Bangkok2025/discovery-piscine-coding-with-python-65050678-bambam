number = int(input("Enter a number: "))
print(f"Multiplication table for {number}:")
for i in range(0, 13):
    print(f"{number} x {i} = {number * i}")