#welcoming the user
print("Welcome to the tip calculator")

#user total bill input (float)
bill = float(input("what was the total bill? $"))

#asking the user how much % of a tip they would like to give
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

#asking the user how many they are (in order to calculate their tips price)
people = int(input("How many people to split the bill? "))

#bill calculation logic
bill_with_tip = tip / 100 * bill + bill
# print(f"Each person should pay: {bill_with_tip:.2f}")

