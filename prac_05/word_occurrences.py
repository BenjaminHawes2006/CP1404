"""
CP1404 Practical - Word Occurrences
Estimate: 20 minutes
Actual:
"""

user_text = input("Enter your sentence: ")
user_words = list(user_text.split(" "))
word_to_count = {}
word_spacer = 0
for word in user_words:
    if len(word) > word_spacer:
        word_spacer = len(word)
    word = word.lower()
    if word not in word_to_count.keys():
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1

for word, count in word_to_count.items():
    print(f"{word:{word_spacer}}:\t{count}")
