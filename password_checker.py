import re


def check_password_strength(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Check number
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Check special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, suggestions


print("=== Password Strength Checker ===")

password = input("Enter a password to check: ")

strength, score, suggestions = check_password_strength(password)

print("\n--- Result ---")
print(f"Strength: {strength}")
print(f"Score: {score}/5")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("\nGreat! Your password meets all the checked requirements.")
