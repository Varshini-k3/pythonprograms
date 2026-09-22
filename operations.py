"""
write a program to input two numbers and checks if:
1.both numbers are greater than 10(using AND)
2.atleast one of the number is lesser than 5(using OR)
3.the 1st number is greater than 2nd(using NOT)
"""
#inputing two numbers
num1 = input("Enter the value of a: ")
num2 = input("Enter the value of b: ")

if( int ( num1 ) > 10 and int ( num2 ) > 10 ):
    print("Both numbers are greater than 10")

if( int ( num1 ) < 5  or int ( num2 )< 5 ):
    print("one of the number is lesser than 5")

if( not (int(num1) < int(num2))):
    print("the 1st number is greater than 2nd")
