import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper  ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

print("What do you choose? Type 0 for rock, 1 for Paper 2 for Scissors.") 
user_choosed = int(input())
print(options[user_choosed])


print("Computer chose:")
computer_choosed = random.randint(0, len(options) - 1)
print(options[computer_choosed])


if computer_choosed == user_choosed:
    print("It's a draw")
    exit(1)

if user_choosed == 0:
    if computer_choosed == 2:
        print("You win")
    else:
        print("You lose")
elif user_choosed == 1:
    if computer_choosed == 0:
        print("You win")
    else:
        print("You lose")
elif user_choosed == 2:
    if computer_choosed == 1:
        print("You win")
    else:
        print("You lose")



