#read 3 from keyboard if 2 numbers are equal are equal validate and print max and min value
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
res = a if a == b and a==c else b if b== c else c
print("Maximum value is: ", res)