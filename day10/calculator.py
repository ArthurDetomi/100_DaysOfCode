import os

from art import logo

def calculate(num1: float, num2: float, ope: str):
    match ope:
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
    return 0.0



selected_first_number = False

num1 = 0.0

while True:
    if not selected_first_number:
        print(logo)
        num1 = float(input("What's the first number?:    "))
    
    ope = input("+\n-\n*\n/\nPick an operation:   ")    

    num2 = float(input("What's the second number?:  "))

    result = calculate(num1, num2, ope)

    print(f"{num1} {ope} {num2} = {result}")

    num1 = result

    choose = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation:  ")

    if choose == 'y':
        selected_first_number = True
    else:
        selected_first_number = False
        os.system("clear")


