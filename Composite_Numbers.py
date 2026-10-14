import math

def is_composite(num):
    # Numbers less than or equal to 1 are neither prime nor composite
    if num <= 1:
        return False
    
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return True  # A factor was found, so it is a composite number
            
    return False  # No factors found, meaning it's a prime number

# Take input from the user
try:
    user_num = int(input("Enter a positive integer: "))
    
    if user_num <= 1:
        print(f"{user_num} is neither a prime nor a composite number.")
    elif is_composite(user_num):
        print(f"{user_num} is a COMPOSITE number.")
    else:
        print(f"{user_num} is a PRIME number (not composite).")
        
except ValueError:
    print("Please enter a valid integer.")
