# * Control Flow Tools

# * switch and case operation is mainly handle by if elif and else operation in python
# * but some how match operation is similar to switch and case operation what we have done in other programming language


# * match statement takes an expression and compares its value to successive patterns given as one or more case blocks
# * this is similar to switch and case in C, Java or JavaScript
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


print(http_error(400))

# * range :- iterate over a sequence of number
# * this is built in function of python

# * range takes 3 arguments
# * first argument as start number
# * second argument as end number
# * third argument as step number
# * range(start, stop, step)
# * if step is not given then default value is 1

# * generate range value from start and end value
print(list(range(5, 10)))

# * generate range value from start, end and with some step
print(list(range(0, 15, 2)))

# * generate range vvalue from negative value of start and end with step
print(list(range(-1, -100, -5)))

# * to get value and index of list
# * enumerate function is used
# * enumerate function have arguments as (iterable object, start = 0 as a default value)
seasons = ["spring", "winter", "summer", "fall"]
print(list(enumerate(seasons)))

# * break statement is a loop control statement. It is used to control the sequence of the loop
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        print(n, "is a prime number")

# * continue : It continues with the next cycle of the nearest enclosing loop.
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

# * pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action
