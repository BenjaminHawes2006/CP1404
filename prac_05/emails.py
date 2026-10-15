"""
CP1404 Practical 5 - Emails
Estimate: 30 minutes
Actual: 38 minutes
"""

user_email = input("Email: ")
email_to_name = {}
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
    email_to_name[user_email] = name
    user_email = input("Email: ")


for email, name in email_to_name.items():
    print(f"{name}\t({email})")