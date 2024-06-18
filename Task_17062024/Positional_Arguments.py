# 1. positional arguments:
# These are the arguments passed to function in correct positional order.

# During a function call, values passed through arguments should be in the order of parameters
# in the function definition. This is called positional arguments.

# Keyword arguments should follow positional arguments only.
def sub(a,b):
    print(a-b)
sub(100,200)
sub(200,100)


# The number of arguments and position of arguments must be matched. If we change the
# order, then result may be changed.
# If we change the number of arguments, then we will get error.