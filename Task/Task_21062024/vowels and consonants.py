# #vowels and consonant
# ch=input("Enter a character: ")
# if ch in ('a','e','i','o','u'):
#     print("Vowel")
# else:
#     print("Consonant")
#
# #even or odd
# num=int(input("Enter a number: "))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")
#
#
# #positive or negative
# num=int(input("Enter a number: "))
#
# if num>0:
#     print("Positive")
# else:
#     print("Negative")
#
# #leap year
# year=int(input("Enter a year: "))
#
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

#largest of three numbers
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter third number: "))
# if a>b and a>c:
#     print("Largest number is ",a)
#
# elif b>a and b>c:
#     print("Largest number is ", b)
#
# #largest of three numbers
# else:
#     print("Largest number is ", c)
#
#sum of n natural numbers
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1, n+1):
#     sum+=i
#     print(sum)
#     print("Sum of first", n, "natural numbers is", sum)
#
# #factorial of a number
# n=int(input("Enter a number: "))
# fact=1
# for i in range(1, n+1):
#     fact*=i
#     print(fact)
#     print("Factorial of", n, "is", fact)
# #factorial of a number using function
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# f = factorial(n)
# print("Factorial of", n, "is", f)

#fibonacci series
n=int(input("Enter a number: "))
a=0
b=1

print(a)

for i in range(2, n+1):
    c=a+b
    a=b
    b=c
    print(c)
    print("Fibonacci series of", n, "is", c)
#fibonacci series using function
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
f = fibonacci(n)
print("Fibonacci series of", n, "is", f)
for i in range(n):
        print(fibonacci(i), end=" ")

