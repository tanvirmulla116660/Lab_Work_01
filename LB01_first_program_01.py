# Python program to greet the user, comment based on age, and give birthday wishes

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age with error handling
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Oops! That doesn't look like a valid age.")
    exit()

# Greet the user
print(f"Hello, {name}!")

# Ask if it's their birthday
birthday = input("Is today your birthday? (yes/no): ").strip().lower()

# Birthday message
if birthday == "yes":
    print("🎉 Happy Birthday! 🎂")

# Give a message based on age
if age < 18:
    print("You're quite young! Enjoy your youth.")
elif age < 65:
    print("Hope you're having a productive and fulfilling day.")
else:
    print("Wishing you a relaxing and enjoyable day!")
