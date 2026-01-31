print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? $10, $12, or $15? $"))
people = float(input("How many people to split the bill? "))
calculate = (total_bill + tip) / people
print(f"Each person should pay: ${calculate}")

