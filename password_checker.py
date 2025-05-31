import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Check length
    if len(password) >= 8:
        feedback.append("✅ Length is at least 8 characters.")
        score += 1
    else:
        feedback.append("❌ Password must be at least 8 characters long.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        feedback.append("✅ Contains an uppercase letter (A–Z).")
        score += 1
    else:
        feedback.append("❌ Add at least one UPPERCASE letter (A–Z).")

    # Check lowercase
    if re.search(r"[a-z]", password):
        feedback.append("✅ Contains a lowercase letter (a–z).")
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a–z).")

    # Check digit
    if re.search(r"[0-9]", password):
        feedback.append("✅ Contains a number (0–9).")
        score += 1
    else:
        feedback.append("❌ Add at least one number (0–9).")

    # Check special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("✅ Contains a special character (!@#$...).")
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$...).")

    # Final strength assessment
    if score == 5:
        strength = "✅ Strong Password!"
    elif score >= 3:
        strength = "⚠️ Moderate Password."
    else:
        strength = "❌ Weak Password!"

    return strength, feedback

def main():
    print("🔐 Password Strength Checker with Feedback 🔐")
    while True:
        password = input("\nEnter your password (or type 'exit' to quit): ")
        if password.lower() == "exit":
            print("Goodbye!")
            break
        strength, tips = check_password_strength(password)
        print("\nPassword Strength:", strength)
        print("\nChecklist:")
        for tip in tips:
            print("-", tip)

if __name__ == "__main__":
    main()
