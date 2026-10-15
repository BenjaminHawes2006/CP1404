"""
CP1404 Practical 5 - Emails
Estimate: 30 minutes
Actual:
"""

user_email = input("Email: ")
email_parts = user_email.split("@")
username = email_parts[0]
name = username.split(".")
print(name)