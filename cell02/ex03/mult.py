number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
result = number1 * number2
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

print("The multiplication result is:", result)