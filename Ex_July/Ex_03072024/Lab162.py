class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


balance = 100
withdraw = int(input("Enter the amount!"))
if withdraw > balance:
    raise Exception("Bal is Low!!")
else:
    print("Remain Bal ", (balance - withdraw))