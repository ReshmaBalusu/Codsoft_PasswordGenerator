import random
import string


def password_generator(leng, difficult):
    if difficult == "1":
        character_set = string.ascii_letters
    elif difficult == "2":
        character_set = string.ascii_letters + string.digits
    elif difficult == "3":
        character_set = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose from Weak, Medium, or Strong.")
        return None

    gen_password = ''.join(random.choice(character_set) for _ in range(leng))

    return gen_password


while True:
    try:
        length = int(input("\nEnter the length for the password: "))
        break
    except ValueError:
        print("Invalid data,Enter a valid length: ")

while True:
    print("1. Weak password")
    print("2. Medium password")
    print("3. Strong password")
    difficulty = input("Enter the desired complexity: ")

    if difficulty in ["1", "2", "3"]:
        break
    else:
        print("Invalid complexity level. Please choose from Weak, Medium, or Strong.")

# Generate and display the password
password = password_generator(length, difficulty)
if password:
    print("Generated Password:", password)
else:
    print("Please enter a password length greater than 0.")
print()
