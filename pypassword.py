letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

import random
print("Welcome to the PyPassword Generator!!")
lenchar = int(input("How many letters do you want in your password? \n "))
lennum = int(input("How many numbers do you want in your password? \n "))
lensym = int(input("How many symbols do you want in your password? \n"))
password_list = []

for char in range(0,lenchar):
    password_list.append(random.choice(letters))
for char in range(0, lennum):
    password_list.append(random.choice(numbers))
for char in range(0, lensym):
    password_list.append(random.choice(symbols))

password =""
for char in password_list:
    password += char
print(f"Your password is: {password}")



        
