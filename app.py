#Utilise the Random Python Library to allow the computer to randomly choose rock, paper, or scissors in each round
import random
choices = ("rock", "paper", "scissors")
count = 0
user_score = 0
computer_score = 0

while count == 0:
    for i in range(5):
        user_choice = input("Choose rock, paper, or scissors: ") #User to now input their choice and compare the computers. 
        computer_choice = random.choice(choices)
        print("Computer chose:", computer_choice)
        if user_choice == computer_choice: #declaring a winner based on rules 
            print("It's a tie") #rock beats scissors, scissors beats paper, and paper beats rock.
            
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
             print("user wins this round")
             user_score += 1
             
        else:
            print("computer wins this round")
            computer_score += 1
            i +=2

        print("score after round", count, ":you", user_score, "-" ,computer_score, "computer")
