print("Welcome to the Tip Calculator!")
bill = float(input("What was the total cost? $"))
tip = int(input("What percentage of tip would you like to give? 5, 10 or 15?"))
people = int(input("How many people to split the bill?"))

bill_with_tip = (tip / 100) * bill + bill
print(f"The total bill value is ${bill_with_tip}")

bill_per_person = bill_with_tip / people
round(bill_per_person, 2)
print(f"Each person should pay ${bill_per_person}")