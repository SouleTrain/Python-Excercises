#Title
import time
print('''
         +----------------------+
         |Enter 2 words and i'll|
         | Tell you if they're  |
         |      Anagrams!       |
         +----------------------+
''')

#Variables
time.sleep(.5)
text1 = input("Enter 1st Word: ")
time.sleep(.5)
text2 = input("Enter 2nd Word: ")
text3 = []
text4 = []
ana = False

#Code
for  char in text1 and text2:
    try:
        if text1.isdigit() or text2.isdigit():
            raise ValueError
    except ValueError:
        print("Words Only Please!")

    if text1.isalpha() and text2.isalpha():
        text3 = list(text1.upper())
        text4 = list(text2.upper())
        text3.sort()
        text4.sort()
        if text3 == text4:
            ana = True
        else:
            ana = False

#Output
if ana == True:
    print(text1, 'and', text2, 'are Anagrams!')
else:
    print(text1, 'and', text2, 'Are Not Anagrams')
