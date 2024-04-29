import string
import random

def generate_password(length=8, use_upper=True, use_numbers=True, use_special=True):
    if use_upper:
        chars = string.ascii_letters
    else:
        chars = string.ascii_lowercase

    if use_numbers:
        chars += string.digits

    if use_special:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    while True:
        mode = input("Please select the mode (default/manual): ").lower()
        if mode == "default":
            print(f"Generated password: {generate_password()}")
            break
        elif mode == "manual":
            while 1:
                try:
                    length = int(input("Enter the desired password length: "))
                    break
                except ValueError:
                    print("Enter a valid number to continue.")
            use_upper = input(f"Use uppercase letters? (y/n): ").lower() == "y"
            use_numbers = input(f"Use numbers? (y/n): ").lower() == "y"
            use_special = input(f"Use special characters? (y/n): ").lower() == "y"
            print(f"Generated password: {generate_password(length, use_upper, use_numbers, use_special)}")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()