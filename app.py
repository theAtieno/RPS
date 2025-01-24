#Utilise the Random Python Library to allow the computer to randomly choose rock, paper, or scissors in each round
import random
choices = ("rock", "paper", "scissors")
user_score = 0
computer_score = 0

while True:
    try:
        total_rounds = int(input("Choose the number of rounds (3 or 5): "))
        if total_rounds in [3, 5]:
            break
        else:
            print("Invalid choice. Please enter 3 or 5.")
    except ValueError:
        print("Please enter a valid number (3 or 5).")

winning_score = (total_rounds // 2) + 1 

round_num = 0
while round_num < total_rounds:
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
        print("Computer wins this round")
        computer_score += 1
        round_num += 1

    if user_score == winning_score:
            print("Congratulations! You win the game!")
            break
    elif computer_score == winning_score:
            print("Computer wins the game! Practise more!")
            break
    
if round_num == total_rounds:
    print("\n Game over!")
    if user_score < winning_score and computer_score < winning_score:
            print("\nGame over!")
            print(f"Final Score - user: {user_score}, {computer_score} : Computer")
    if user_score > computer_score:
            print("Congratulations! You win the game!")
    elif user_score < computer_score:
            print("Computer wins the game! Practise more!")
    else:
            print("It's a tie overall!")