"""
CP1404 Practical 5 - Emails
Estimate: 30 minutes
Actual:
"""

user_email = input("Email: ")
while user_email != "":
    email_parts = user_email.split("@")
    username = email_parts[0]
    split_names = username.split(".")
    names = []
    for name_part in split_names:
        names.append(name_part)
    name = " ".join(names).title()
    name_confirmation = input(f"Is your name {name}? [y/n] ")
    if name_confirmation == "y" or name_confirmation == "":
        pass
    else:
        name = input("What is your name? ")
    print(f"Name: {name}")
    user_email = input("Email: ")