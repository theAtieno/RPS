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

for round_num in range(1, total_rounds + 1):
    print(f"\nRound {round_num} of {total_rounds}")

user_choice = input("Choose rock, paper, or scissors: ") #User to now input their choice and compare the computers. 
    
computer_choice = random.choice(choices)
print("Computer chose:", computer_choice)
if user_choice == computer_choice: #declaring a winner based on rules
    print("It's a tie") 
    print("It's a tie") #rock beats scissors, scissors beats paper, and paper beats rock.
            
elif (user_choice == "rock" and computer_choice == "scissors") or \
    (user_choice == "paper" and computer_choice == "rock") or \
    (user_choice == "scissors" and computer_choice == "paper"):
    print("user wins this round")
    user_score += 1

else:
    print("Computer wins this round")
    computer_score += 1
    