#Utilise the Random Python Library to allow the computer to randomly choose rock, paper, or scissors in each round
import random
choices = ("rock", "paper", "scissors")
computer_choice = random.choice(choices)
for _ in range(3):
    print(computer_choice)
