# Enhanced Python program with more personalized interaction

# Ask the user for their name
name = input("What is your name? ")

# Ask the user for their age with error handling
try:
    age = int(input("How old are you? "))
except ValueError:
    print("Oops! That doesn't look like a valid age.")
    exit()

# Ask if it's their birthday
birthday = input("Is today your birthday? (yes/no): ").strip().lower()

# Ask the user about their favorite hobby
hobby = input("What's your favorite hobby? ")

# Greet the user
print(f"\n--- Hello, {name}! ---")

# Birthday message
if birthday == "yes":
    print("🎉 Happy Birthday! 🎂")

# Age-based message
if age < 18:
    age_msg = "You're quite young! Enjoy your youth."
elif age < 65:
    age_msg = "Hope you're having a productive and fulfilling day."
else:
    age_msg = "Wishing you a relaxing and enjoyable day!"

print(age_msg)

# Final summary
print(f"\nHere's what I learned about you:")
print(f"Name   : {name}")
print(f"Age    : {age}")
print(f"Hobby  : {hobby}")
if birthday == "yes":
    print("Today is your birthday! 🎉")

print("\nThanks for chatting with me! 😊")
