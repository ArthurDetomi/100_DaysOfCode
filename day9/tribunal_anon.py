from art import logo

import os

def get_winner_by_dict(dic):
    max_bid = 0
    name_winner = ""
    
    for key in dic:
        if dic[key] > max_bid:
            max_bid = dic[key]
            name_winner = key
    
    return name_winner

print(logo)

bets = {}

while True:
    name = input("What is your name?: ") 
    bid = float(input("What is your bid ?: $"))
    
    bets[name] = bid
    
    print("Are there any other bidders? Type 'yes' or 'no'.")
    option = input()
    
    if option == 'no':
        name_winner = get_winner_by_dict(bets)        
        print(f"The winner is {name_winner} with a bid of ${bets[name_winner]}")
        break
    
    os.system("clear")
    
    
    
    
    
    