# Python program to greet the user and comment based on age

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age
age = int(input("How old are you? "))

# Greet the user
print(f"Hello, {name}!")

# Give a message based on age
if age < 18:
    print("You're quite young! Enjoy your youth.")
elif age < 65:
    print("Hope you're having a productive and fulfilling day.")
else:
    print("Wishing you a relaxing and enjoyable day!")
