import secrets
import string

def generate_password(length=12, use_digits=True, use_special=True, use_uppercase=True):
    characters = string.ascii_lowercase  # Start with lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Generate a secure random password
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    try:
        length = int(input("Enter password length (minimum 8): "))
        if length < 8:
            print("Password length should be at least 8 characters for security.")
            return None

        use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'

        return length, use_digits, use_special, use_uppercase
    except ValueError:
        print("Invalid input. Please enter numeric values where required.")
        return None

def main():
    print("Welcome to the Secure Password Generator!")

    while True:
        preferences = get_user_preferences()
        if preferences:
            length, use_digits, use_special, use_uppercase = preferences
            password = generate_password(length, use_digits, use_special, use_uppercase)
            print("\nGenerated Password: ", password)

        another = input("\nGenerate another password? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Thank you for using the Password Generator. Stay secure!")
            break

if __name__ == "__main__":
    main()