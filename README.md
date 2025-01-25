# Password Generator in Python

The Password Generator is a Python application that helps users create secure, random passwords based on their preferences. Users can specify the desired length and choose to include numbers, special characters, and uppercase letters to enhance password strength.

<h2>Key Features</h2>

- 🔢 Customizable Length: Choose the desired password length
- 🔡 Character Options: Include/exclude uppercase letters, digits, and special characters
- 🛡️ Secure Generation: Uses Python's secrets module for strong randomness
- 📋 Copy to Clipboard (Optional): Easily copy the generated password
- 🔄 Multiple Password Generation: Generate multiple passwords in one go

<h2>Technologies Used:</h2>

- Python

<h2>Code Implementation (CLI Version)</h2>

```

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

```

<h2>How to Use This  Application</h2>

1. Save the script as password_generator.py.
2. Run the script using: ```python password_generator.py```
3. Follow the prompts to customize and generate a secure password.

<h3>Example Usage:</h3>

```

Welcome to the Secure Password Generator!
Enter password length (minimum 8): 12
Include digits? (yes/no): yes
Include special characters? (yes/no): yes
Include uppercase letters? (yes/no): yes

Generated Password:  dF#8g!T$2vA1

Generate another password? (yes/no): no
Thank you for using the Password Generator. Stay secure!

```

<h2></h2>
<p align="center">
  <a href="https://github.com/rlangc/Test_RCL.git"><b>Return to Home</b></a>
