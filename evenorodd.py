#program to check if a number is even or odd

number = int(input("Enter an integer:"))

#check if number is perfectly divided by 2
if number % 2 == 0:
    print(f"{number}is an even number.")
else:
    print(f"{number}is an odd number.")
