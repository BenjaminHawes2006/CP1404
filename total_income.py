"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_counter = int(input("How many months? "))

    for month in range(1, month_counter + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month_counter + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month} - Income: ${income:10} Total: ${total:10}")


main()