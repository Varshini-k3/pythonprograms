# Taking user inputs for Principal, Rate, and Time
principal = float(input("Enter the principal amount (P): "))
rate = float(input("Enter the annual interest rate (R %): "))
time = float(input("Enter the time period in years (T): "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

# Calculating total amount payable
total_amount = principal + simple_interest

# Displaying the results formatted to 2 decimal places
print(f"\n--- Results ---")
print(f"Simple Interest: {simple_interest:.2f}")
print(f"Total Amount (Principal + Interest): {total_amount:.2f}")
