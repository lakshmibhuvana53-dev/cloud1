# programming for typeconversion and type casting
user_name=input("What is ur name ? \n")
length_of_name=len(user_name)
print(type(user_name))
print(type(length_of_name))
print("Number of letters your Name holds is : " + str(length_of_name))

# conditional operators and a example program
print("Welcome to Roller Coaster!")
height = int(input("What is your height in cm? \n"))
if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
     


    #  to check if a number is even or odd

    number_to_check = int(input("Enter the number you want to check : \n"))
    if number_to_check % 2==0:
        print("The number you entered is an even number")
    else:
        print("The number you entered is an odd number")