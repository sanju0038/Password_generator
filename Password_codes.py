import random

Capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Small_letters = "abcdefghijklmnopqrstuvwxyz"
Numbers = "0123456789"
Special_Characters = "@#$&"

def PasswordGenerator(length=8):
    total_characters = Capital_letters + Small_letters + Numbers + Special_Characters
    password = "".join(random.choice(total_characters) for _ in range(length))
    return password

# Prompt the user and validate input
try:
    n = int(input("Enter the desired password length: "))
    if n > 12:
        print("ERROR !: The Password length should be less than or equal to 12")
    else:
        result = PasswordGenerator(n)
        print("Generated Password:", result)

        # Counters for each character type
        s_count = 0
        c_count = 0
        n_count = 0
        sp_count = 0

        # Check each character type in the generated password
        for i in result:
            if i in Capital_letters:
                c_count += 1
            elif i in Small_letters:
                s_count += 1
            elif i in Numbers:
                n_count += 1
            elif i in Special_Characters:
                sp_count += 1

        # Validate if the password is strong
        if s_count > 0 and c_count > 0 and sp_count > 0 and n_count > 0:
            print("Password is Strong")
        else:
            print("Password is Weak")
except ValueError:
    print("Invalid input! Please enter an integer for the password length.")
