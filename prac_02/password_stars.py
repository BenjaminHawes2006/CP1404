
def main():
    minimum_password_length = 8
    password = input("Enter your password: ")
    while len(password) < minimum_password_length:
        print("Error: Password too short!")
        password = input("Enter your password: ")
    print("*" * len(password))

main()
