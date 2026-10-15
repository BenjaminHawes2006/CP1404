"""
CP1404 Practical - Word Occurrences
Estimate: 20 minutes
Actual:
"""

user_text = input("Enter your sentence: ")
user_words = list(user_text.split(" "))
word_to_count = {}

for word in user_words:
    if word not in word_to_count.keys():
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1

print(word_to_count)
