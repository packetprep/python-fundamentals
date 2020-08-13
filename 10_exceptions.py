## Exception handling in python

#basic
try:
    i = int("apple")
    print(i)
except:
    print("This is an error")

# Named errors
try:
    i = 10/0
except(ZeroDivisionError):
    print("You cannot divide a number with zero.")
except(ValueError):
    print("There is value error")
except:
    print("Unknown Error")
else:
    print("All is well")

# Error Reporting
def func(*args):
    l = len(args)

    if(l<1):
        raise TypeError("Arguments cannot be less than one")
    for i in args:
        print(i)
try:
    func()
except TypeError as e:
    print(f"TypeError: {e}")
