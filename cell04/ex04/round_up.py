import math

num_str = input("Give me a number: ")

try:
    num = float(num_str)
    rounded = math.ceil(num)
    print(f"The rounded-up value is {rounded}.")
except ValueError:
    print("This is not a valid number.")