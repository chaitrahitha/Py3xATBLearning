#    print("dads") # IndentationError: unexpected indent
# result = 5 +"5" #TypeError: unsupported operand type(s) for +: 'int' and 'str'
# int("pramod") # ValueError: invalid literal for int() with base 10: 'pramod'
# print(undefined_variable) # NameError: name 'undefined_variable' is not defined

# my_list = [1, 2, 3]
# print(my_list[3]) #IndexError: list index out of range

# my_dict = {"a": 1, "b": 2}
# print(my_dict["c"]) # KeyError: 'c'

#result = 10 / 0 # ZeroDivisionError: division by zero

# import non_existent_module ModuleNotFoundError: No module named 'non_existent_module'

try:
    import math
    math.exp(1000) # OverflowError: math range error
except Exception as e:
    print(e)