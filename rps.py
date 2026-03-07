paper ='''          
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'       
'''
rock = '''       ________         
         ___.--"          "\'.        
  ------f"               // \\\        
        |                    |||                    
        |                    |||                     
    ----L_-XXX-.             .|'                   
                "\   -<_____///                    
                  \___)     -"      
'''

scissors = '''    _    
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
import random
print("Welcome to Rock, Paper, Scissors!")
user_choice = int(input("Type 0 for rock, 1 for papaer, 2 for scissors: "))
if user_choice >= 3 or user_choice < 0:
    print("You have entered an input that is out of range. You loose!")
elif user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
   
    print(user_choice)
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:        
    print(paper)

elif computer_choice == 2:
    print(scissors)

    print(computer_choice)

if user_choice == computer_choice:
    print("It's a Tie !")
elif user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice ==1:
    print("You WON the Game !!")
else:
    print("Computer Won the game !!")


