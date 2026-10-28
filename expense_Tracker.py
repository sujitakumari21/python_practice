#EXPENSE_TRACKER


expenses = []

def add_expense():
    item = input("Expense name: ")
    amount = float(input("Amount: "))
    
    expenses.append((item, amount))
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found!")
        return

    total = 0
    print("\nExpenses:")
    
    for item, amount in expenses:
        print(f"{item} : ₹{amount}")
        total += amount

    print("Total Expense =", total)

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")