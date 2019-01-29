"""
Simple method
"""

def print_string(my_string=""):
    """
    takes one argument and prints it
    """
    if my_string != '':
        print(my_string)
    else:
        print("")

if __name__ == '__main__':
    print_string("Hello!")
    print_string()
