import csv

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Expense Name: ")
        amount = float(input("Amount: "))
        category = input("Category: ")

        expenses.append([name, amount, category])

        with open("expenses.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, amount, category])

        print("Expense Added Successfully!")

    elif choice == "2":
        print("\nExpense History")
        for exp in expenses:
            print(exp)

    elif choice == "3":
        total = sum(exp[1] for exp in expenses)
        print("Total Expense =", total)

    elif choice == "4":
        print("Thank You")
        break

    else:
        print("Invalid Choice")