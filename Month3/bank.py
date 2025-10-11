class User():

    def __init__(self, name, username, password, balance):
        self.name = name
        self.username = username
        self.password = password
        self.balance = balance

    def view_balance(self):
        return f"{self.name.title()}, you have a total balance of {self.balance} in the Bank"

    def deposit(self):
        dp = int(input(f"{self.name.title()}, please enter the amount that you would like to deposit: "))
        self.balance += dp
        print("Thankyou for depositing")
        return f"Your balance is now {round(self.balance, 2)}"

    def withdraw(self):
        wd = int(input(f"{self.name.title()}, please enter the amount that you would like to withdraw: "))
        while True:
            if wd > self.balance:
                print("You cannot withdraw more than your balance. Please try again.")
            else:
                print("Thankyou for withdrawing.")
                break
        self.balance -= wd
        return f"Your balance is now {round(self.balance, 2)}"


    def options(self):
        print("Here are a list of options, please choose the option you want:")
        while True:
            option_choice = int(input("1) See Balance \n2) Deposit \n3) Withdraw \n4) Quit \n"))
            if option_choice == 1:
                print(self.view_balance())
                break
            elif option_choice == 2:
                print(self.deposit())
                break
            elif option_choice == 3:
                print(self.withdraw())
                break
            elif option_choice == 4:
                break
            else:
                print("Invalid input. Please try again.")


print("Welcome to  Kaavya's Bank!")

users = {}

while True:
    user_type = input("Are you a new user? Yes or No? ")

    if user_type == 'yes':
        print("Thankyou for trusting Kaavya's Bank. We promise to provide you with a smooth experience")
        name = input("Please enter your name: ")
        username = input("Please enter a valid username: ")
        password = input("Please provide a strong password: ")
        balance = float(input("How much balance do you have? "))
        new_user = User(name, username, password, balance)
        users[username] = new_user
        new_user.options()
        print("Thankyou for creating a bank account!")

    elif user_type == 'no':
        old_user = input("Please enter your username: ")
        if old_user in users:
            old_user = users[old_user]
            password_validation = input("Enter your password: ")
            while True:
                if password_validation == old_user.password:
                    old_user.options()
                    break
                else:
                    print("Wrong password. Try again.")
        else:
            print("That username does not exist please try again.")
