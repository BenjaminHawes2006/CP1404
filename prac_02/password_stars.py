
def main():
    minimum_password_length = 8
    password = get_password(minimum_password_length)
    print_password(password)

def print_password(password: str):
    print("*" * len(password))

def get_password(minimum_password_length: int) -> str:
    password = input("Enter your password: ")
    while len(password) < minimum_password_length:
        print("Error: Password too short!")
        password = input("Enter your password: ")
    return password

main()
