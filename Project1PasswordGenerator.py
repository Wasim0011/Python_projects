import random

letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '(', ')', ',', '+']
n_letters=int(input("How many letters you want in your Password?\n"))
passwordList = []   # empty list to store password
for i in range(1, n_letters+1):
    char = random.choice(letters)
    passwordList += char    # storing password character by character
n_numbers = int(input("How many numbers you want in your Password?\n"))
for i in range(1, n_numbers+1):
    char = random.choice(numbers)
    passwordList += char    # storing password character by character
n_symbols = int(input("How many symbols you want in your Password?\n"))
for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    passwordList += char    # storing password character by character
# print(passwordList)
random.shuffle(passwordList)    # shuffle passwordList
# print(passwordList)
password = ""   # empty password string
for i in passwordList:
    password += i   # storing shuffle passwordList one by one in password string
print("Your Generated PASSWORD is: " + password)
