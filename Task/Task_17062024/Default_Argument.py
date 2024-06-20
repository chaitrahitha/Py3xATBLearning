# 3. Default Arguments:

# Default arguments are values that are provided while defining functions.
# The assignment operator = is used to assign a default value to the argument.
# Default arguments become optional during the function calls.
# If we provide a value to the default arguments during function calls, it overrides the default value.
# The function can have any number of default arguments.
# Default arguments should follow non-default arguments.
# Sometimes we can provide default values for our positional arguments.

# Eg:
def wish(name="Guest"):
    print("Hello",name,"Good Morning")

wish("QAC" )
wish()

# Output
# Hello QAC Good Morning
# Hello Guest Good Morning

# If we are not passing any name, then only default value will be considered.

# ***Note:

# After default arguments we should not take non default arguments

# > valid  :  def wish(name="Guest",msg="Good Morning"):
# > valid :  def wish(name,msg="Good Morning"):
# > Invalid :  def wish(name="Guest",msg):
# Syntax Error: non-default argument follows default argument

