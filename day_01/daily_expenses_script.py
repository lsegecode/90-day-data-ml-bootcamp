# daily_expenses_script.py

def get_expenses():
    """Ask the user for daily expenses and return them as a list of floats."""
    expenses = []
    print("Enter your daily expenses (type 'done' when finished):")
    while True:
        entry = input("Expense: $")
        if entry.lower() == 'done':
            break
        try:
            expenses.append(float(entry))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return expenses


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
    print(f"Average daily expense: ${average:.
