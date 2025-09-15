print(" Welcome to Kaavya's Pet Store! ")
pet_prices = {
    "dog": 100,
    "cat": 200,
    "bird": 300,
    "fish": 400,
    "snake": 500,
    "hamster":  600,
    "rabbit": 700,
}

print("Our Pet Prices:")
print(pet_prices)
print()

# Accessing values or looking up prices
print("Looking up individual prices:")
print(f"Dog costs: {pet_prices['dog']}")
print(f"Fish costs: {pet_prices['fish']}")
print()

# Adding new items (adding new pets to the store)
print("Adding new pets to our store!")
pet_prices["turtle"] = 800
pet_prices["guinnea pig"] = 900

print("Updated inventory:")
print(pet_prices)
print()

# Updating items (updating prices)
print("Having a sale! Updating prices!")
pet_prices["hamster"] = 200
pet_prices["snake"] = 100

print("Sale Prices:")
print(pet_prices)
print()

# Complex dictionaries (adding pet details)
print("Detailed pet information:")
pet_details = {
    "dog": {
        "price": 300,
        "age": "8 months",
        "breed": "Golden retriever",
        "vaccinated": True
    },
    "cat": {
        "price": 200,
        "age": "3 years",
        "breed": "Syrian",
        "vaccinated": True
    },
    "hamster": {
        "price": 400,
        "age": "6 months",
        "breed": "British Hamster",
        "vaccinated": True
    },
    "snake": {
        "price": 200,
        "age": "8 months",
        "breed": "Python",
        "vaccinated": False
    }
}

# Refer to a particular complex dictionary
print("Dog details:")
dog_info = pet_details["dog"]
print(f"Price: ${dog_info['price']}")
print(f"Age: {dog_info['age']}")
print(f"Breed: {dog_info['breed']}")
print(f"Vaccinated: {dog_info['vaccinated']}")
print()

# Interactive Pet Store

print("Welcome Customer! Let's help you shop!")
print("Available pets:")
for pet_name, price in pet_prices.items():
    print(f"  {pet_name.title()}: ${price}")
print()

customer_pet = input("Which pet would you like to buy?").lower().strip()

# Check if pet exists
if customer_pet in pet_prices:
    print(f"Great choice! The {customer_pet} cost ${price}")

else:
    print("Sorry, we don't have that pet in stock :(")

# Dictionary methods - useful tools:
print("Dictionary Tools:")
print(f"All pet types: {list(pet_prices.keys())}")
print(f"All prices: {list(pet_prices.values())}")
print(f"Number of pet types: {len(pet_prices)}")

# Removing an item from the dictionary
print("Removing the turtle from the dictionary")
del pet_prices["turtle"]
print(pet_prices)
