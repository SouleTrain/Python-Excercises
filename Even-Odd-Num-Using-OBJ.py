#Importing just for fun and fanciness
import time
import os

#Declaring empty list for appending through loop
even_list = []
odd_list = []  

#Function for clearing console for fanciness
def clear_term():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        os.system('clear')

#Object (I know scripting is easier but im just practicing obj approach)         
class Number:
    def __init__(self):
        self.__x = x
    def even(x):
        even = False
        if x % 2 == 0:
            even = True
        if even == True and x != 0:
            even_list.append(x)
    def odd(x):
        odd = False
        if x % 2 != 0:
            odd = True
        if odd == True:
            odd_list.append(x)
              
#Script utilizing object
print("Here's a list of EVEN numbers between 1 and 25")
time.sleep(2)

for x in range(26):
    Number.even(x)
print(even_list)

time.sleep(4)
clear_term()

print("Here's a list of ODD numbers bewtween 1 and 25 ")
time.sleep(2)

for x in range(26):
    Number.odd(x)
print(odd_list)
