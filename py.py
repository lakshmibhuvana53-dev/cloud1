import random
user_choice = int(input("What do you want choose? Type 0 for Rock,1 for Paper and 2 for Scissors \n"))
computer_choice = random.randint(0,2)
print(f"Computer chose{computer_choice}")
if(user_choice < 0 or user_choice > 2):
    print("Invalid input")
elif(user_choice == computer_choice):
    print("The game is draw...")
elif(user_choice == 1 and computer_choice == 0 or
    user_choice == 2 and computer_choice == 1 or
    user_choice == 1 & computer_choice == 0 ):
    print("You Won !!")
else:
    print("Computer Won !!")


