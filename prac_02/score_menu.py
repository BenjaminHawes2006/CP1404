"""
CP1404 Benjamin Hawes: Do-from-scratch exercise
"""

def main():
    user_score = int(input("Enter your score (0-100): "))
    user_input = provide_menu()
    while user_input != "Q":
        if user_input == "G":
            user_score = int(input("Enter your score here: "))
            print(f"Score received: {user_score}")
            user_input = provide_menu()
        elif user_input == "P":
            print(f"Your result is {determine_grade(user_score)}")
            user_input = provide_menu()
        elif user_input == "S":
            if user_score < 0 or user_score > 100:
                print("Invalid score")
            else:
                print_stars(user_score)
            user_input = provide_menu()
    print("Farewell")

def print_stars(number_of_stars):
    print("*" * number_of_stars)

def determine_grade(score) -> str:
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def provide_menu():
    user_input = input("""Menu: 
    G - Enter a valid score
    P - Print result
    S - Show stars
    Q - Quit
    >>>""")
    return user_input


main()