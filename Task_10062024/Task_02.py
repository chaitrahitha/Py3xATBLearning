# Develop a Python script that calculates the square and cube of a given number.
# num = 2 sq - 4, c = 8
num = 2
square = num ** 2
cube = num ** 3

print(f"The square of {num} is {square}.")
print(num," cubed is ",cube)


# Create a program that takes two numbers as input and prints whether the first number is
# greater than, less than, or equal to the second number.

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if(n1>n2):
    print("n1 is greater than n2")
elif(n1<n2):
    print("n1 is smaller than n2")
else:
    print("n1 is equals to n2")