"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    user_score = float(input("Enter score: "))
    print(f"User's grade is {determine_grade(user_score)}")
    random_score = random.randint(0,100)
    if determine_grade(user_score) == "Excellent":
        print("Well done, you get a prize!")
    print(f"Random Score: {random_score}")
    print(f"Random grade is {determine_grade(random_score)}")

def determine_grade(score) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()