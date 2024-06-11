#Explain the difference between the = operator and the == operator in Python.

# = Operator (Assignment Operator):
x = 10  # Assigns the value 5 to the variable x
y = "Hello"  # Assigns the string "Hello" to the variable y
z= 15.6  # Assigns the float 15.6 to the variable z


# == Operator (Equality Comparison Operator):
# The == operator is used to compare two values for equality.
# It returns True if the values on both sides are equal, and False otherwise.
a = 2
b = 2
print(a == b)  # Returns True because a and b have the same value
c = "Hello"
d = "World"
print(c == d)  # Returns False because c and d have different values



# What does the ** operator do in Python, and how is it used?

# The ** operator is used for exponentiation(power) in Python.
# It is a binary operator that takes two operands: the base and the exponent.

result = 2 ** 3  # 2 raised to the power of 3
print(result)  # Outputs 8

result = 5 ** 2  # 5 raised to the power of 2
print(result)  # Outputs 25



# What does the ^ operator do in Python, and in what context is it commonly used?

# The ^ operator is a bitwise XOR (exclusive OR) operator.
# It compares each bit of its first operand to the corresponding bit of its second operand.
# If one bit is 0 and the other bit is 1, the corresponding result bit is set to 1.
# Otherwise, it is set to 0.

x = 10  # Binary: 1010
y = 4   # Binary: 0100
result = x ^ y  # Binary result: 1110
print(result)  # Outputs 14

# Binary breakdown:
# 1010
# 0100
# ----
# 1110 (which is 14 in decimal)