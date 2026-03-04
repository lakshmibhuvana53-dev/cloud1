# programming for typeconversion and type casting
user_name=input("What is ur name ? \n")
length_of_name=len(user_name)
print(type(user_name))
print(type(length_of_name))
print("Number of letters your Name holds is : " + str(length_of_name))

# conditional operators and a example program
print("Welcome to Roller Coaster!")
height = int(input("What is your height in cm ? "))
if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")