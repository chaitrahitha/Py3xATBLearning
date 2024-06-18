# 3. Variable length arguments:
# Sometimes we can pass variable number of arguments to our function,such type of
# arguments are called variable length arguments.

# We can declare a variable length argument with * symbol as follows
#             def f1(*n):

# We can call this function by passing any number of arguments including zero number.
# Internally all these values represented in the form of tuple.

# Eg:

def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("The Sum=",total)

sum()
sum(10)
sum(10,20)
sum(10,20,30,40)

# Output
# The Sum= 0
# The Sum= 10
# The Sum= 30
# The Sum= 100

# Note:
# We can mix variable length arguments with positional arguments.

#Ex:

def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)

f1(10)
f1(10,20,30,40)
f1(10,"A",30,"B")

# Output
# 10
# 10
# 20
# 30
# 40
# 10
# A
# 30
# B

# Note:After variable length argument,if we are taking any other arguments then we
# should provide values as keyword arguments.

# Eg:

def f1(*s,n1):
    for s1 in s:
        print(s1)
        print(n1)

f1("A","B",n1=10)
# Output
# A
# B
# 10

# f1("A","B",10) ==>Invalid
# TypeError: f1() missing 1 required keyword-only argument: 'n1'



