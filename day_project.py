import requests
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("This is my ultimate function")
        func()
    return wrapper



add = lambda a,b: a+b

@my_decorator
def add(arg1=4, *args):
    total_args = 0
    for num in args:
        print(args)
    return total_args


print(add(1,2,3,4,5))
