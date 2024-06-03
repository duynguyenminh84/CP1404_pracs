
"""constant"""



"""main function"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius"""
    print(MENU)
    choice = input(">>> ").upper()
    temperature= int(input("Please enter your temperature: "))
    if choice== "C":
     convert_celsius_to_fahrenheit(temperature)
    else:
     convert_fahrenheit_to_celsius(temperature)

"""other functions"""
def convert_celsius_to_fahrenheit(celsius):
 return print(celsius * 9 / 5 + 32)

def convert_fahrenheit_to_celsius(fahrenheit):
 return print(5 / 9 * (fahrenheit - 32))

 """Calling main function"""

main()