# 2. keyword arguments:
# The arguments which are passed through the keyword are identified using the names
# assigned to them. Here’s an example to illustrate this.


# Functions can also be called using keyword arguments of the form kwarg=value.

# During a function call, values passed through arguments don’t need to be in the
# order of parameters in the function definition. This can be achieved by keyword arguments.
# But all the keyword arguments should match the parameters in the function definition.
# We can pass argument values by keyword i.e by parameter name.
# Eg:
def wish(name,msg):
    print("Hello",name,msg)
wish(name="Basavana Gouda",msg="Good Morning")
wish(msg="Good Morning",name="Basavanagouda")

# O/P:
# Hello Basavana Gouda Good Morning
# Hello Basavanagouda Good Morning

# Here the order of arguments is not important but number of arguments must be matched.

# Note:

# We can use both positional and keyword arguments simultaneously. But first we have to
# take positional arguments and then keyword arguments,otherwise we will get syntaxerror.

def wish(name,msg):
    (print("Hello",name,msg))
# > valid
wish("QACircle","GoodMorning")
# > valid
wish("QACircle",msg="GoodMorning")
# > invalid :   wish(name="QACircle","GoodMorning")
# Syntax Error: positional argument follows keyword argument