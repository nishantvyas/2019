import functools

def decorate_function(function):
    @functools.wraps(function)
    def function_to_be_wrapped():
        print("Decorating the function here. Before.")
        function()
        print("Decorating the function here. After.")

    return function_to_be_wrapped

@decorate_function
def my_function():
    print("This is what my_function does")

def decorate_function_with_args(argument):
    def decorate_function_with_args_func(function):
        @functools.wraps(function)
        def function_to_be_wrapped_with_args(*args, **kwargs):
            print("Decorating the function here. Before.")
            if argument == 1:
                function(*args, **kwargs)
            else:
                pass
            print("Decorating the function here. After.")
        return function_to_be_wrapped_with_args
    return decorate_function_with_args_func

@decorate_function_with_args(1)
def my_function_with_args(x, y):
    print(x+y)

def main():
    my_function()
    my_function_with_args(100, 1)

if __name__ == '__main__':
    main()
