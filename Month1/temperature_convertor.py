#Python temperature convertor

print("Welcome to the temperature convertor!")

temp = float(input("What is the temperature in the room at present?"))
unit = input("Is the temperature in Celcius or Farenheit? (C or F):").strip()

if unit == "C":
    temperature = temp * 1.8 + 32
    print(f"The temperature in the room is {round(temperature,2)}°F ")
elif unit == "F":
    temperature = (temp - 32) / 1.8
    print(f"The temperature in the room is {round(temperature, 2)}°C ")
else:
    print("Value entered is invalid")
