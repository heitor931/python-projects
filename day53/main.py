def my_decorator(func):
    def wrapper_func():
        print('Hello, this is my decorator')
        func()
        func()
    return wrapper_func()

@my_decorator
def my_func():
    print('This is my function')
