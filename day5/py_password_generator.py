import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password_builder = []

for i in range(0, nr_letters):
    choice = random.choice(letters)

    password_builder.append(choice)

for i in range(0, nr_numbers):
    choice = random.choice(numbers)


    password_builder.append(choice)

for i in range(0, nr_symbols):
    choice = random.choice(symbols)

    password_builder.append(choice)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
result = ''.join(password_builder)

random.shuffle(password_builder)

result_hard = ''.join(password_builder)

print(f"Your password is -- Easy level: {result}")
print(f"Your password is -- Hard level: {result_hard}")


