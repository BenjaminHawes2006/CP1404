
def main():
    password_character_count = get_password()
    print_stars(password_character_count)

def print_stars(password_character_count: int):
    print("*" * password_character_count)

def get_password() -> int:
    password = input("Enter your password: ")
    password_character_count = len(password)
    return password_character_count

main()
