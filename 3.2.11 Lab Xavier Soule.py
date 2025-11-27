word_without_vowels = ""

word = input("Enter Word Here: ")
word = word.upper()


for letter in word:
    if letter not in ("AEIOU"):
        word_without_vowels += letter
print(word_without_vowels)
