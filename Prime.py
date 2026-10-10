# Program to find prime numbers between 1 and 100

print("Prime numbers between 1 and 100 are:")

for num in range(1, 101):
    # Prime numbers must be greater than 1
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
