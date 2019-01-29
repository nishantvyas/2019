"""
List Tuple & Set
"""

def my_list():
    my_list = [1,2,3]
    print(my_list)

def my_tuple():
    my_tuple = (1,2,3)
    print(my_tuple)

def my_set():
    my_set = {1,2}
    print(my_set.union({3,4}))
    print(my_set.intersection({2}))


if __name__ == '__main__':
    my_list()
    my_tuple()
    my_set()
