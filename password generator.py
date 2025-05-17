import random
import string

#func get pass length and return random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be positive number.")
            return
        password = generate_password(length)
        print("The random password:", password)
    except ValueError:
        print("Please enter valid number.")

if __name__ == "__main__":
    main()
