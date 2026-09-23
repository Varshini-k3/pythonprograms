# Python program to calculate the factorial of a number

def calculate_factorial(num):
    # Factorial is not defined for negative numbers
    if num < 0:
        return "Factorial does not exist for negative numbers."
    # The factorial of 0 and 1 is always 1
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        # Loop from 2 up to the number itself
        for i in range(2, num + 1):
            result *= i
        return result

# Example usage:
number = 5
print(f"The factorial of {number} is {calculate_factorial(number)}")
