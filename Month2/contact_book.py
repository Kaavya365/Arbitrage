print("Welcome to Kaavya's Contact book!")

contacts = {
    "kaavya": 7337814489,
    "manjari": 9740119475,
    "kumanan": 9880119475,
    "vim": 9741116111,
}

print("Available Contacts:")
print(contacts)
print()

print("Looking up individual phone numbers:")
print(f"Kaavya's Phone Number is {contacts['kaavya']}")
print(f"Kumanan's Phone Number is {contacts['kumanan']}")
print(f"Manjari's Phone Number is {contacts['manjari']}")
print(f"Vim's Phone Number is {contacts['vim']}")

print("Adding new items")
contacts["ramya"] = 9535300455
print("New Contact Book list:")
print(contacts)
print()

print("Deleting items")
del contacts["vim"]
print("New Contact Book list:")
print(contacts)
print()

# Listing using 'for' loops
for name, number in contacts.items():
    print(f"The Phone Number of {name} is {number}")

# Making it interactive
contact_name = input("Please provide the name of the person you want the phone number of").strip().lower()
if contact_name in contacts:
    print(f"The Phone Number of {contacts[contact_name]}")
else:
    print("Sorry, that name doesn't exist in our contact book :(")
    print(f"All the names available: {list(contacts.keys())}")
