
def logging_decorator(func):
    def wrapper(*args):
        a = func(*args)

        print(f"You called\n {func.__name__}{args}\n It returned: {a}")
    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1 ,2 ,3)