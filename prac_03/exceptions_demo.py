"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When we enter an invalid number like a float, or a special character

2. When will a ZeroDivisionError occur?
When we enter 0 as a denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes, to set a condition of denominator != 0

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Cannot divide by zero!")

except ValueError:
    print("Numerator and denominator must be valid numbers!")


print("Finished.")