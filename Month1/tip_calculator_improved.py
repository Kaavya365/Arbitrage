print("Welcome to the Tip Calculator!")
bill = float(input("What was the total cost? $"))
if 100 <= bill < 200:
    print("The tip percentage on the base cost will be 5%")
    tip = 5
    tip_value = tip / 100 * bill
    bill_with_tip = tip/100 * bill + bill
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
split_bill= round(split_bill, 2)
print(f"Each person has to pay ${split_bill}")
