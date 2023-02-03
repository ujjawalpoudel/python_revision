# * start with args and kwargs in python
# * *args and **kwargs allow you to pass multiple arguments or keyword arguments to a function.


def adder(x, y, z):
    print("sum:", x + y + z)


adder(10, 12, 13)

# * In above example, if we pass a keyword argument to a function more than 3
# * for example adder(5,10,15,20,25)
# * at that time TypeError: adder() takes 3 positional arguments but 5 were given, this type of error pop up
# * to minimize such errors, we have to use


# * Passing Multiple Arguments to a Function
# * *args can be really useful, because it allows you to pass a varying number of positional arguments
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print(my_sum(1, 2, 3))


# * note args is just a variable name, we can change this one
# sum_integers_args_2.py
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result


print(my_sum(1, 2, 3))
