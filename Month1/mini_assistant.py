print("Hello! I'm Baymax, your personal assistant!")

while True:
    project = input("Which program would you like to run? "
                    "a. Note-Taking Program "
                    "b. Number Guessing Game "
                    "c. Quiz "
                    "d. Tip Calculator "
                    "e. Unit Convertor ").strip().lower()

    if project == "a":
        import datetime
        import os
        import tkinter as tk


        def create_directory():
            current_date = datetime.date.today()
            directory_name = current_date.strftime('%Y-%m-%d')
            if not os.path.exists(directory_name):
                os.mkdir(directory_name)


        def save_entry():
            current_date_time = datetime.datetime.now()
            file_name = current_date_time.strftime('%Y-%m-%d %H-%M-%S')
            entry = text_entry.get('1.0', 'end-1c')
            directory_name = current_date_time.strftime('%Y-%m-%d')
            file_path = os.path.join(directory_name, file_name + '.txt')
            with open(file_path, 'w') as file:
                file.write(entry)


        root = tk.Tk()
        root.title('Diary')

        text_entry = tk.Text(root, height=20, width=20)
        text_entry.pack()

        save_button = tk.Button(root, text='Save', command=save_entry)
        save_button.pack()
        quit_button = tk.Button(root, text='Quit', command=root.quit)
        quit_button.pack()

        create_directory()

        root.mainloop()

    elif project == "b":
        import random

        print("Welcome to my Number Guessing Game!")

        number = random.randint(1, 100)
        guess = 0

        while guess != number:
            guess = int(input("Enter Guess!"))

            if guess < number:
                print("Too Low! Guess Higher!")
            elif guess > number:
                print("Too High! Guess Lower!")
            else:
                print("You Won!")
    elif project == "c":
        # Kaavya's python quiz using tuples

        questions = ("Who was the king of the Greek gods?",
                     "What is the Roman name for the goddess Athena?",
                     "Which hero killed the Minotaur?",
                     "In Roman mythology, who was the king of the gods?",
                     "Who was punished to hold up the sky for eternity?",
                     "What was the Roman name for the Greek god Hades?",
                     "Who gave fire to mankind and was punished by Zeus?",
                     "Which goddess is associated with love and beauty? (Greek name)",
                     "In Roman mythology, Mars was the god of what?",
                     "Who was the messenger god in Greek mythology?")

        options = (("A. Hades", "B. Zeus", "C. Apollo", "D. Poseidon"),
                   ("A. Juno", "B. Diana", "C. Minerva", "D. Vesta"),
                   ("A. Heracles", "B. Theseus", "C. Perseus", "D. Odysseus"),
                   ("A. Mars", "B. Jupiter", "C. Saturn", "D. Neptune"),
                   ("A. Atlas", "B. Cronus", "C. Prometheus", "D. Ares"),
                   ("A. Vulcan", "B. Pluto", "C. Saturn", "D. Mercury"),
                   ("A. Hermes", "B. Prometheus", "C. Hephaestus", "D. Apollo"),
                   ("A. Hera", "B. Aphrodite", "C. Demeter", "D. Artemis"),
                   ("A. War", "B. Love", "C. Wisdom", "D. Harvest"),
                   ("A. Apollo", "B. Hermes", "C. Ares", "D. Dionysus"))

        answers = ("B", "C", "B", "B", "A", "B", "B", "B", "A", "B")
        guesses = []
        score = 0
        question_num = 0

        for question in questions:
            print("----------------------------------")
            print(question)
            for option in options[question_num]:
                print(option)

            guess = input("Enter your first guess (A, B, C, D):").strip().upper()
            guesses.append(guess)
            if guess == answers[question_num]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT! ")
                print(f"{answers[question_num]} is the correct answer!")
            question_num += 1

        print("-----------------------------")
        print("         RESULTS!            ")
        print("-----------------------------")

        print("answers: ", end="")
        for answer in answers:
            print(answer, end="")
        print()

        print("guesses: ", end="")
        for guess in guesses:
            print(guess, end="")
        print()

        score = int(score / len(questions) * 100)
        print(f"Your score is: {score}%")

    elif project == "d":
        print("Welcome to the Tip Calculator!")
        bill = float(input("What was the total cost? $"))
        if 100 <= bill < 200:
            print("The tip percentage on the base cost will be 5%")
            tip = 5
            tip_value = tip / 100 * bill
            bill_with_tip = tip / 100 * bill + bill
            print(f"The value of the tip to be paid is ${tip_value}")
            print(f"The total bill value is ${bill_with_tip}")

        elif 200 <= bill < 500:
            print("The tip percentage on the base cost will be 8%")
            tip = 8
            tip_value = tip / 100 * bill
            bill_with_tip = tip / 100 * bill + bill
            print(f"The value of the tip to be paid is ${tip_value}")
            print(f"The total bill value is ${bill_with_tip}")

        elif 500 <= bill < 1000:
            print("The tip percentage on the base cost will be 10%")
            tip = 10
            tip_value = tip / 100 * bill
            bill_with_tip = tip / 100 * bill + bill
            print(f"The value of the tip to be paid is ${tip_value}")
            print(f"The total bill value is ${bill_with_tip}")

        elif bill >= 1000:
            print("The tip percentage on the base cost will be 15%")
            tip = 15
            tip_value = tip / 100 * bill
            bill_with_tip = tip / 100 * bill + bill
            print(f"The value of the tip to be paid is ${tip_value}")
            print(f"The total bill value is ${bill_with_tip}")

        else:
            print("No tip will apply since the cost is lower than $100")

        people = int(input("How many people are splitting the bill?"))
        split_bill = bill_with_tip / people
        split_bill = round(split_bill, 2)
        print(f"Each person has to pay ${split_bill}")

    elif project == "e":
        print("Welcome to the unit convertor!")
        type = str(input(
            "Which conversion would you like to do? a. Weight conversion (Kgs to Lbs and vice-versa) b. Temperature conversion (Celsius to Farenheit and vice-versa)"))

        if type == "b":
            # Python temperature convertor

            print("Welcome to the temperature convertor!")

            temp = float(input("What is the temperature in the room at present?"))
            unit = input("Is the temperature in Celcius or Farenheit? (C or F):").strip()

            if unit == "C":
                temperature = temp * 1.8 + 32
                print(f"The temperature in the room is {round(temperature, 2)}°F ")
            elif unit == "F":
                temperature = (temp - 32) / 1.8
                print(f"The temperature in the room is {round(temperature, 2)}°C ")
            else:
                print("Value entered is invalid")

        elif type == "a":
            # Python weight convertor

            weight = float(input("Enter your weight"))
            unit = input("Kilograms or Pounds? (K or L):").strip()
            if unit == "K":
                weight = weight * 2.205
                unit = "Lbs."
                print(F"Your weight is: {round(weight, 1)} {unit}")
            elif unit == "L":
                weight = weight / 2.205
                unit = "Kgs."
                print(f"Your weight is: {round(weight, 1)} {unit}")
            else:
                print(f"{unit} was not valid")

        else:
            print("Value invalid!")

    else:
        print("Invalid Input!")
    input("\nPress Enter to return to main menu...")

    print("Program ended.")
