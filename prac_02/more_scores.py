"""
CP1404 Benjamin Hawes: Program for practical 2 practice Task
"""
import random

def main():
    number_of_scores = int(input("Enter a number of scores: "))
    with open("results.txt", "w", encoding="utf-8") as file:
        for i in range(0, number_of_scores):
            random_score = random.randint(0, 100)
            file.write(f"{random_score} is {determine_grade(random_score)}\n")

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