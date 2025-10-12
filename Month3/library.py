print("Welcome to Kaavya's library!")

books = [
    'Lord of the Rings',
    'Harry Potter',
    'Hunger Games',
    'Divergent',
    'The Seven Husbands of Evelyn Hugo',
    'The Silent Patient',
    'The Girl on the Train'
]

class Lib():
    def __init__(self, name, email, phone_no, username, password):
        self.name = name
        self.email = email
        self.phone_no = phone_no
        self.username = username
        self.password = password
        self.borrowed_books = {}

    def list_books(self):
        print("Here is the list of available books: ")
        for index, book in enumerate(books):
            print(f"#{index + 1} : {book}")

    def list_books_personal(self):
        print("Here is the list of books you have with you: ")
        for index, (book, date) in enumerate(self.borrowed_books.items()):
            print(f"#{index + 1} : {book} (borrowed on {date})")
    def issue(self):
        self.list_books()
        borrow = int(input("Which book would you like to borrow? (Mention the #) "))
        date = input("What is today's date? ")
        book_name = books[borrow - 1]
        self.borrowed_books[book_name] = date
        print(f"Thankyou {self.name}, for borrowing {book_name} on {date}")
        print("List of your borrowed books: ")
        print(list(self.borrowed_books))

    def returns(self):
        if not self.borrowed_books:
            print("You haven't borrowed any books yet")
        else:
            self.list_books_personal()
            returning = int(input("Which book would you like to return? (Mention the #) "))
            date = input("What is today's date? ")
            books_list = list(self.borrowed_books)
            book_name = books_list[returning-1]
            del self.borrowed_books[book_name]
            print(f"Thankyou {self.name}, for returning {book_name} on {date}")
            print("New list of your borrowed books: ")
            print(list(self.borrowed_books))

    def options(self):
        while True:
            choice = int(input(f"What would you like to do today?\n1. Issue a book\n2. Return a book\n3. Quit\n"))
            if choice == 1:
                self.issue()
            elif choice == 2:
                self.returns()
            elif choice == 3:
                break
            else:
                print("Invalid input. Please try again.")



users = {}
while True:
    user_type = input("Are you a new user? Yes or No? ")
    if user_type == 'yes':
        print("Thankyou for choosing Kaavya's library! Please complete the registration process.")
        name = input("Please provide your full name: ")
        email = input("Please provide your email id: ")
        phone_no = input("Please provide your phone number: ")
        username = input("Kindly create a valid username: ")
        password = input("Provide a strong password: ")

        new_user = Lib(name, email, phone_no, username, password)
        users[username] = new_user
        new_user.options()

    elif user_type == 'no':
        old_user = input("Enter username: ")
        while True:
            if old_user in users:
                old_user = users[old_user]
                password_verification = input("Enter password: ")
                while True:
                    if password_verification == old_user.password:
                        old_user.options()
                        break
                    else:
                        print("Incorrect password. Please  try again")
            else:
                print("Sorry, this username does not exist. Please try again.")
