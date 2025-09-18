expense_name = []
expense_type = []
expense_amount = []
groceries = []
food = []
clothing = []
rent = []
entertainment = []
miscellaneous = []

def addExp():
    expName = input("What did you spend on? ")
    while True:
        expType = input("What was the category of expenditure? A. Groceries, B. Food, C. Clothing, D. Rent, E.Entertainment, F. Miscellaneous ").strip().upper()
        if expType in ["A", "B", "C", "D", "E", "F"]:
            break
        else:
            print("Invalid input. Please try again.")

    expAmount = float(input("What was the exact amount spent? "))

    if expType == "A":
        groceries.append(expAmount)
        category = "Groceries"
    elif expType == "B":
        food.append(expAmount)
        category = "Food"
    elif expType == "C":
        clothing.append(expAmount)
        category = "Clothing"
    elif expType == "D":
        rent.append(expAmount)
        category = "Rent"
    elif expType == "E":
        entertainment.append(expAmount)
        category = "Entertainment"
    else:
        miscellaneous.append(expAmount)
        category = "Miscellaneous"

    expense_amount.append(expAmount)
    expense_name.append(expName)
    expense_type.append(category)

    print(f"The expense: {expName} of amount {expAmount}, within the category {category} has been added to the list of expenses.")
    totalExp()

def totalExp():
        print("The expenses are listed as follows:")
        print(f"Total Expenses: {sum(expense_amount)}")
        print(f"Groceries: {sum(groceries)}")
        print(f"Food: {sum(food)}")
        print(f"Clothing: {sum(clothing)}")
        print(f"Rent: {sum(rent)}")
        print(f"Miscellaneous: {sum(miscellaneous)}")

def listExp():
    if not expense_amount:
        print("No expenditures have been made yet")
    else:
        for index, (name, category, amount) in enumerate(zip(expense_name, expense_type, expense_amount)):
            print(f"#{index} : {name} | {category} | {amount}")

def deleteExp():
    listExp()
    try:
        expenseToDelete = int(input("Enter the # of the expense you would like to delete."))
        if not expenseToDelete < 0 and expenseToDelete <= len(expense_name):
            expense_name.pop(expenseToDelete)
            expense_type.pop(expenseToDelete)
            expense_amount.pop(expenseToDelete)
            print("Expense has been removed")
        else:
            print(f"Expense: {expenseToDelete} was not found.")
    except:
        print("Invalid Input")

print("Welcome to my Python Tracker!")
while True:
    print("Please select one of the following options:")
    print("1. Add an expense")
    print("2. Delete an expense")
    print("3. View the list of expenses")
    print("4. View the totals of all expenses")
    print("5. Quit")
    choice = input("Enter your choice: ").strip().lower()

    if choice == "1":
        addExp()

    elif choice == "2":
        deleteExp()

    elif choice == "3":
        listExp()

    elif choice == "4":
        totalExp()

    elif choice == "5":
        break

    else:
        print("Invalid input. Please try again.")
