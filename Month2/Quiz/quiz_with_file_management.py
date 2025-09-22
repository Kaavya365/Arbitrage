def main():

    # Get user to input quiz
    quiz = get_user_choice()

    # Convert quiz name to filename
    quiz_filename = get_quiz_filename(quiz)

    # Get the required quiz from a CSV file
    run_quiz(quiz_filename)

def get_user_choice():
    quiz_list = [
        "Greek Mythology Quiz",
        "Indian Mythology Quiz",
        "Egyptian Mythology Quiz",
        "Roman Mythology Quiz",
        "Norse Mythology Quiz"
    ]
    while True:
        print("Select a quiz: ")
        value_range = f"1 - {len(quiz_list)}"
        for i, quiz_name in enumerate(quiz_list):
            print(f"{i+1}. {quiz_name}")
        quiz_choice = int(input(f"Enter the Quiz Number: [{value_range}]")) - 1

        if quiz_choice in range(len(quiz_list)):
            selected_quiz = quiz_list[quiz_choice]
            return selected_quiz
        else:
            print("Invalid input. Please try again.")

def get_quiz_filename(selected_quiz):
    quiz_files = {
        "Greek Mythology Quiz": "quiz1.csv",
        "Indian Mythology Quiz": "quiz2.csv",
        "Egyptian Mythology Quiz": "quiz3.csv",
        "Roman Mythology Quiz": "quiz4.csv",
        "Norse Mythology Quiz": "quiz5.csv"
    }
    return quiz_files[selected_quiz]

def run_quiz(quiz_filename):
    questions = []
    answers = []
    correct_answers = 0
    with open(quiz_filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            question, option_a, option_b, option_c, option_d, answer = line.strip().split(",")
            print(f"Question: {question}")
            print(f"A. {option_a}")
            print(f"B. {option_b}")
            print(f"C. {option_c}")
            print(f"D. {option_d}")
            print()
            user_input = input("Pick an answer [A, B, C, D]:").strip().upper()
            print()
            if user_input == answer:
                print("Correct Answer!")
                correct_answers += 1
            else:
                print(f"Wrong answer, the correct answer was {answer}")

        print(f"You scored {correct_answers} out of {len(lines)}")

if __name__ == "__main__":
    main()
