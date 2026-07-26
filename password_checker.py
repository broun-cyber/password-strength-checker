import re


def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


password = input("Enter a password to check: ")

strength, suggestions = check_password_strength(password)

print(f"\nPassword Strength: {strength}")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
