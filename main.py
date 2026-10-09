#welcoming the user
print("Welcome to the tip calculator")

#user total bill input (float)
bill = float(input("what was the total bill? $"))

#asking the user how much % of a tip they would like to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

#asking the user how many they are (in order to calculate their tips price)
people = int(input("How many people to split the bill? "))

#bill calculation logic
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2) #rounds a number to a specified number of decimal places
print(f"Each person should pay: ${final_amount}") #the f lets you mix text and math variables together easily

