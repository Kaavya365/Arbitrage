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

options = (("A. Hades","B. Zeus","C. Apollo","D. Poseidon"),
           ("A. Juno","B. Diana","C. Minerva","D. Vesta"),
           ("A. Heracles","B. Theseus","C. Perseus","D. Odysseus"),
           ("A. Mars","B. Jupiter","C. Saturn","D. Neptune"),
           ("A. Atlas","B. Cronus","C. Prometheus","D. Ares"),
           ("A. Vulcan","B. Pluto","C. Saturn","D. Mercury"),
           ("A. Hermes","B. Prometheus","C. Hephaestus","D. Apollo"),
           ("A. Hera","B. Aphrodite","C. Demeter","D. Artemis"),
           ("A. War","B. Love","C. Wisdom","D. Harvest"),
           ("A. Apollo","B. Hermes","C. Ares","D. Dionysus"))

answers = ("B","C","B","B","A","B","B","B","A","B")
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


