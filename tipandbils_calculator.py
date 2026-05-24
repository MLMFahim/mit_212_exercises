# 1. Gather input from the user
print("--- Welcome to the Bill Splitter ---")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? (e.g., 15, 18, 20): "))
people = int(input("How many people are splitting the bill? "))

# 2. Do the math
tip_amount = total_bill * (tip_percentage / 100)
final_bill = total_bill + tip_amount
per_person_amount = final_bill / people

# 3. Display the results
# The :.2f forces Python to format the number to exactly 2 decimal places (cents)
print("\n--- Results ---")
print(f"Total tip amount: ${tip_amount:.2f}")
print(f"Total bill with tip: ${final_bill:.2f}")
print(f"Each person should pay: ${per_person_amount:.2f}")
