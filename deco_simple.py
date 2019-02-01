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

def main():
    my_function()


if __name__ == '__main__':
    main()
