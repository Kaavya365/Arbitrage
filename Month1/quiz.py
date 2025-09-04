print("Welcome to Kaavya's quiz!")

while True:

    type = input("Which topic would you like to be quizzed on? "
             "a. Capitals of the world "
             "b. Countries by their landmarks "
             "c. Geography facts and figures ")

    if type == "a":
        print("Awesome! Here's your first question!")
        correct = 0
        Q1 = input("What is the capital of Colombia?").strip().lower()
        if Q1 == "bogota":
            correct = correct+1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q2 = input("What is the capital of Morocco?").strip().lower()
        if Q2 == "rabat":
            correct = correct+1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q3 = input("What is the capital of Ireland?").strip().lower()
        if Q3 == "dublin":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q4 = input("What is the capital of Malaysia?").strip().lower()
        if Q4 == "kuala lumpur":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q5 = input("What is the capital of New Zealand?").strip().lower()
        if Q5 == "wellington":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

    elif type == "b":
        print("Awesome! Here's your first question!")
        correct = 0
        Q1 = input("In which country can you find the leaning tower of Pisa?").strip().lower()
        if Q1 == "italy":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q2 = input("In which country can you find the Great Barrier Reef?").strip().lower()
        if Q2 == "australia":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q3 = input("In which country can you find the Great wall of China?").strip().lower()
        if Q3 == "china":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q4 = input("In which country can you find the largest salt flats?").strip().lower()
        if Q4 == "bolivia":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q5 = input("In which country can you find the set of the Lord of the Rings?").strip().lower()
        if Q5 == "new zealand":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

    elif type == "c":
        print("Awesome! Here's your first question!")
        correct = 0
        Q1 = input("The Tropic of ______ passes through the middle of India.").strip().lower()
        if Q1 == "cancer":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q2 = input("What is the largest island in the world? ").strip().lower()
        if Q2 == "greenland":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q3 = input("Which country has the highest number of natural lakes in the world?").strip().lower()
        if Q3 == "canada":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q4 = input("Which river's source is in the Ethiopian Highlands?").strip().lower()
        if Q4 == "nile" or Q4 == "river nile":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

        Q5 = input("What is a narrow strip of land connecting two larger landmasses called? ").strip().lower()
        if Q5 == "isthmus":
            correct = correct + 1
            print("Correct answer! Moving on...")
        else:
            print("Sorry :( That's the wrong answer...")

    else:
        print("Invalid Input! Try again.")

    print(f"Congratulations on completing my quiz! Your score is {correct}")

    quiz_again = input("Would you like to play again?").strip().lower()
    if quiz_again != "yes":
        print("Thanks for playing")
        break
