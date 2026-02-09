# def add(a, b):
#     "Return the sum of two arguments"
#     return a + b

# add(1, 3);

# function docstring 就是给函数的一种说明书！
# 可以通过help函数进行查阅
def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b

help(add);