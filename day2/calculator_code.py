print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
qtd_person = int(input("How many people to split the bill?"))


total_bill =  bill * (1 + (tip/100))
total_bill_per_person = round(total_bill / qtd_person, 2)

print(f"Each person should pay: ${total_bill_per_person:.2f}")

