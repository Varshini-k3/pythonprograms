# Recursive function to find the nth Fibonacci number
def fibonacci(n):
    # Base cases: F(0) = 0, F(1) = 1
    if n <= 1:
        return n
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Number of terms to print
terms = 10

print("Fibonacci Sequence (Python):")
for i in range(terms):
    print(fibonacci(i), end=" ")
