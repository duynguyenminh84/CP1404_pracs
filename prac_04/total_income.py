"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    income_calculation(incomes)


def income_calculation(incomes):
    total = 0
    for month, income in enumerate(incomes,1):
        total+= income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income,total))

main()




