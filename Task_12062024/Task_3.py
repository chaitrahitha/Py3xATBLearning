# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24


n = int(input("Enter the number: "))
fact = 1
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    # Calculate factorial
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is {fact}.")
