# String Reverse
# 3-4 ways to do this in Python

str = "Hello World"
print("".join(reversed(str)))
# Output: dlroW olleH

str = "Hello World"
print(str[::-1])
print("Hello World"[::-1])
# Output: dlroW olleH

def reverse_string(str):
    """
    Reverse a string using a loop
    """
    reversed_str = ""
    for i in range(len(str)-1, -1, -1):
        reversed_str += str[i]
    return reversed_str
print(reverse_string("Hello World"))

