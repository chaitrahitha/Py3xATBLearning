# def outer_function():
#     var1 = 30
#     def inner_function():
#         print(var1)
#
#     inner_function()
#
#     def inner_function2():
#         print(var1)
#
#     inner_function2()
#
#
# outer_function()

def outerring():
    print("outer function started")
    def innerring():
        print("inner function started")
    print("outer function ended")
    innerring()
    # return innerring
f1= outerring()
# f1= outerring()
# f1()
# f1()
# f1()