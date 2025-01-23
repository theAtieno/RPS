import random
game = ("Rock", "Paper", "Scissors")
my_choice = input("Choose Rock, Paper or Scissors:")
computer_choice = random.choice(game)
print("You chose:", my_choice)
print("Computer chose:", computer_choice)
