#Title/ Variables
text = input("Enter Number: ")
length = 0

#Code
while True:
    if text.isalpha() or len(text) > 8:
        print('Invalid Format')
        break
    if length < len(text):
        total = sum(int(i) for i in text)
        total2 = str(total)
        total3 = sum(int(i) for i in total2)
        length += 1

#Output
    if length == 1:
        print(total3)
        break
