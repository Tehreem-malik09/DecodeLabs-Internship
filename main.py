import string


def check_password_strength(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if any(char.isupper() for char in password):
        score += 1

    # Number Check
    if any(char.isdigit() for char in password):
        score += 1

    # Special Character Check
    if any(char in string.punctuation for char in password):
        score += 1

    # Strength Evaluation
    if score <= 1:
        return "Weak Password"
    elif score <= 3:
        return "Medium Password"
    else:
        return "Strong Password"


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    password = input("Enter your password: ")

    result = check_password_strength(password)

    print("\nPassword Analysis Result")
    print("-" * 25)
    print(f"Strength: {result}")


if __name__ == "__main__":
    main()