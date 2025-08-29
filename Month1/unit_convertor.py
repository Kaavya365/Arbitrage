print("Welcome to the unit convertor!")
type = str(input("Which conversion would you like to do? a. Weight conversion (Kgs to Lbs and vice-versa) b. Temperature conversion (Celsius to Farenheit and vice-versa)"))

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
