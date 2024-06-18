#Arbitrary Keyword Arguments (**kwargs)

#If you have a function that accepts a varying number of arguments, you can use *args for non-keyword arguments
# and **kwargs for keyword arguments.
# The *args will collect all the remaining positional arguments into a tuple,
# while **kwargs will collect all the remaining keyword arguments into a dictionary.

#Eg:
def my_function(*args, **kwargs):
    print("Non-keyword arguments:", args)
    print("Keyword arguments:", kwargs)

# Note: We can declare key word variable length arguments also. For
# this we have to use **.
#             def f1(**n):
# We can call this function by passing any number of keyword arguments. Internally these
# keyword arguments will be stored inside a dictionary.
# Eg:
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)

display(n1=10,n2=20,n3=30)
display(Rno=100,name="Basava",marks=34,subject='Python')
print("*******************************")
def display(**qac):
    for k,v in qac.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(Rno=100,name="Basava",marks=34,subject='Python')

# Output

# n1 = 10
# n2 = 20
# n3 = 30
# Rno = 100
# name = Basava
# marks = 34
# subject = Python
# *******************************
# n1 = 10
# n2 = 20
# n3 = 30
# Rno = 100
# name = Basava
# marks = 34
# subject = Python

def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")