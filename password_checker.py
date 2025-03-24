import re

def check_password_strength(password):
    strength_score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&* etc.).")

    # Strength rating
    strength_levels = {
        5: "Very Strong 💪",
        4: "Strong ✅",
        3: "Moderate ⚠️",
        2: "Weak ❌",
        1: "Very Weak ❌❌",
        0: "Extremely Weak ❌❌❌"
    }

    strength_result = strength_levels[strength_score]
    
    return strength_result, feedback


# User Input
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve:")
        for tip in suggestions:
            print(f" - {tip}")
