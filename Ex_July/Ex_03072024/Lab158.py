# try, except and finally

try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1/num2
except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
else:
    print(f'Result is {result}')
finally:
    print("I will be executed anyhow!!")