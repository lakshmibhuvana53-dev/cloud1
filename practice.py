# conditional operators and a example program
print("Welcome to Roller Coaster!")
height = int(input("What is your height in cm? \n"))
bill = 0
if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age : \n"))
    if age < 12:
        bill = 5
        print("Please pay $5 for children.")
    elif age <= 18:
        bill = 7
        print("Please pay $7 for youth.")
    else:
        bill = 12
        print("Please pay $12 for adults.")
    wants_photo = input("Do you want a photo taken ? type Y for yes and N for No.")
    if wants_photo == "Y":
        # add +3
        bill += 3
        print(f"Your final bill is : ${bill}")
            
else:
    print("Sorry, you have to grow taller before you can ride.")
     


      