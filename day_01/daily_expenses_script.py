# daily_expenses_script.py
import csv


def get_expenses():
    """Ask the user for daily expenses and return them as a list of floats."""
    expenses = []
    dates = []
    print("Enter your daily expenses (type 'done' when finished):")
    while True:
        entry = input("Expense: $")
        if entry.lower() == 'done':
            break
        try:
            expenses.append(float(entry))
        except ValueError:
            print("Invalid input. Please enter a number.")
            
        date = input("Insert the date in DD/MM format:")
        dates.append(date)

    return expenses, dates


def calculate_stats(expenses):
    """Return total, average, max, and min of expenses."""
    if not expenses:
        return 0, 0, 0, 0
    total = sum(expenses)
    average = total / len(expenses)
    maximum = max(expenses)
    minimum = min(expenses)
    return total, average, maximum, minimum


def display_summary(total, average, maximum, minimum):
    """Print the results nicely."""
    print("\n--- Expense Summary ---")
    print(f"Total spent: ${total:.2f}")
    print(f"Average daily expense: ${average:.2f}")
    print(f"Maximum expense: ${maximum:.2f}")
    print(f"Minimum expense: ${minimum:.2f}")


def savedataincsv(expenses, data, dates):
    with open(expenses, mode='w', newline='') as csvfile:
        cswriter = csv.writer(csvfile)
        cswriter.writerow(data)
        cswriter.writerow(dates)

def main():
    expenses, dates = get_expenses()
    print(dates)
    total, average, maximum, minimum = calculate_stats(expenses)
    display_summary(total, average, maximum, minimum)
    savedataincsv('example.csv', expenses, dates)


if __name__ == "__main__":
    main()
