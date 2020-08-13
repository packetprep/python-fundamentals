# # Functions in Python

# Basic function
def basic_func():
	print("This is a basic function")
# basic_func()

# function with arguments
def arg_func(arg1,arg2):
	print(arg1,arg2)
# arg_func(2,3)
# print(arg_func(4,3))
# print(arg_func)

# function with return value
def add(a,b):
	s = a+b
	return s
# print(add(4,3))

# function with default value
def power(n,x=1):
	result = 1;
	for i in range(x):
		result = result * n
	return result
# print(power(2,3))
# print(power(2))
# print(power(x=3,n=2))

# function with varaible arguments
def var_args_func(*args):
	s = 0;
	for a in args:
		s = s + a
	return s
# print(var_args_func(4,2,4,5))
# print(var_args_func(4,2,4,5,10))

# global & local variables
a = 10
print(a)a

def func():
	global a
	a=12
	print(a)

func()

print(a)