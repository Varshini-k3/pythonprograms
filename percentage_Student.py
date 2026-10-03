# Input marks for 6 subjects
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))
m6 = float(input("Enter marks for Subject 6: "))

# Calculate total and percentage
total = m1 + m2 + m3 + m4 + m5 + m6
percentage = (total / 600) * 100

print("Total Marks =", total)
print("Percentage =", percentage, "%")

# Check pass or fail
if percentage > 40:
    print("PASS")
else:
    print("FAIL")
