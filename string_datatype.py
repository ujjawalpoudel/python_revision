# * Study String Data Type of Python
# * We can use ('....') = single quotes
# * We can use ("....") = double quotes
# * Both of these work in Python

# * Single Quote
print("Single Quote")

# * Double Quote
print("Double Quote")

# * Use \ to escape the single quote
print("Use ' to escape the single quote")

# * \t use to tab
print("Tab \t Tab is used to escape the single quote")

# * use \n to create a new line
print("Use \n to create a new line")

# * use r befor quote to ignore special characters
# * r in print statements state as raw strings

# * not use of r raw strings
print("C:\some\name")

# * use r befor quote
print(r"C:\some\name")


# * For multi-line strings
# * use """.......""" or use '''....'''
print(
    """
      Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
      """
)

# * String can also concatenated (glued together)
print("ujjawal" + "poudel")

# * String repetation using *
print(3 * "ujjawal")


# * Index in string
word = "Python"

# * character in position 0
print(word[0])

# * character in position 3
print(word[3])

# * negative index is used to count from right side
print(word[-1])

# * index 0 and -0 are same
# * negative index always start from -1
print(word[0], word[-0])

# * slicing in string
# * [first:last] first number is always included and last number is always excluded

# * start from index 0 and end in index 1 (i.e. exclude position 2)
print(word[0:2])

# * start from index 2 and upto 4 i.e. exclude position 5
print(word[2:5])

# * character from the beginning to position 2 (excluded)
print(word[:2])

# * characters from position 4 (included) to the end
print(word[4:])

# * characters from the second-last (included) to the end
print(word[-2:])
