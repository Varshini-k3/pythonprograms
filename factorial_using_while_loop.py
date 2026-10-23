# Python program to find the factorial of a number using a while loop

num = int(input("Enter a number: "))
factorial = 1
i = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    while i <= num:
        factorial *= i
        i += 1
    print(f"The factorial of {num} is {factorial}.")
