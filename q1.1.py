import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please ahoose at least one characters set (letters, numbers, or symbols).")
        return None

    password = ' '.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("welcome to the Password Generator!")

    try:
        length = int(input("Enter the password length: "))
        use_letters = input("Include letters (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols (yes/no): ").lower() == 'yes'
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
        return

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print("\nGenerated Password:", password)
if __name__ == "__main__":
    main()
