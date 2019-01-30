def calling_function(function):
    return function()

def multiply():
    return 5 * 5

def main():
    print(calling_function(multiply))

if __name__ == '__main__':
    main()
