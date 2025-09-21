from expense import Expense
import calendar
import datetime
def main():
    print("Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000
    # Get user to input expense
    expense = get_user_expense()

    # Write the expense into a file
    save_expense_to_file(expense, expense_file_path)

    # Read the file and summarise all expenses
    summarize_expense(expense_file_path, budget)

def get_user_expense():
    print("Getting User Expense!")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "Groceries",
        "Food",
        "Clothing",
        "Rent",
        "Entertainment",
        "Miscellaneous"
    ]
    while True:
        print("Select a category: ")
        for index, category_name in enumerate(expense_categories):
            print(f"  {index + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number:{value_range} ")) - 1
        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid input. Please try again")

def save_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path, budget):
    print("Summarizing User Expense")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by Category:")
    for key, amount in amount_by_category.items():
        print(f"   {key}: ${amount: .2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"You've spent ${total_spent: .2f} this month!")

    remaining_budget = budget - total_spent
    print(f"Budget remaining: ${remaining_budget: .2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"Remaining days in the current month: {remaining_days}")

    daily_budget = remaining_budget / remaining_days
    print(f"Daily budget: ${daily_budget: .2f}")
if __name__ == "__main__":
    main()
