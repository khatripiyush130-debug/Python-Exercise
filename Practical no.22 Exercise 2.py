FILE = "expenses.txt"
expenses = []
def add_expense():
    category = input("Enter category: ")
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Enter a valid amount.")
        return
    expenses.append([category, amount])
    with open(FILE, "a") as f:
        f.write(f"{category}|{amount}\n")
    print("Expense saved!")
def show_report():
    total = 0
    categories = {}
    for category, amount in expenses:
        total += amount
        categories[category] = (
            categories.get(category, 0) + amount
        )
    print("\nTotal Expenses:", total)
    for category, amount in categories.items():
        percentage = amount / total * 100 if total else 0
        print(category, amount, f"{percentage:.1f}%")
def set_budget():
    try:
        budget = float(input("Enter total budget: "))
        if budget < 0:
            print("Budget cannot be negative.")
            return
    except ValueError:
        print("Enter a valid budget.")
        return
    total = sum(amount for category, amount in expenses)
    if total > budget:
        print("Alert! Budget exceeded.")
    else:
        print("You are within your budget.")
def main():
    try:
        with open(FILE, "r") as f:
            for line in f:
                category, amount = line.strip().split("|")
                expenses.append([category, float(amount)])
    except FileNotFoundError:
        pass
    while True:
        print("\n1. Add Expense")
        print("2. View Report")
        print("3. Set Budget")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_report()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
main()
