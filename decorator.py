def decorator(func):
    def wrapper():
        print("Before the original function call.")
        func()
        print("After the original function call.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()