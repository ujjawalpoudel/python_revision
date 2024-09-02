# Import deque from collections to use it as a stack
from collections import deque


# Define a Stack class using deque for storing elements
class Stack:
    def __init__(self):
        self.container = deque()  # Initialize an empty deque

    def push(self, value):
        self.container.append(value)  # Add an element to the top of the stack

    def pop(self):
        return self.container.pop()  # Remove and return the top element

    def is_empty(self):
        return len(self.container) == 0  # Check if the stack is empty

    def size(self):
        return len(self.container)  # Return the number of elements in the stack


# Function to reverse a string using the Stack class
def reverse_string(s):
    stack = Stack()

    # Push each character of the string onto the stack
    for char in s:
        stack.push(char)

    reversed_str = ""
    # Pop each character from the stack to build the reversed string
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str


# Test the reverse_string function

print(reverse_string("We will conquer COVI-19"))  # Output: 91-IVOC ereuqnoc lliw eW
print(reverse_string("I am the king"))  # Output: gnik eht ma I


# Function to check if the parentheses are balanced
def is_balanced(string):
    stack = Stack()

    # Dictionary to match opening and closing parentheses
    matching_parentheses = {")": "(", "}": "{", "]": "["}

    # Iterate over each character in the string
    for char in string:
        # If character is an opening bracket, push it onto the stack
        if char in "({[":
            stack.push(char)
        # If character is a closing bracket
        elif char in ")}]":
            # If stack is empty, it means there's no opening bracket to match
            if stack.is_empty():
                return False
            # Pop the last opening bracket and check if it matches the current closing bracket
            top = stack.pop()
            if matching_parentheses[char] != top:
                return False

    # If stack is empty, all parentheses were matched correctly
    return stack.is_empty()


print(is_balanced("({a+b})"))  # Output: True
print(is_balanced("))((a+b}{"))  # Output: False
print(is_balanced("((a+b))"))  # Output: True
print(is_balanced("((a+g))"))  # Output: True
print(is_balanced("))"))  # Output: False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # Output: True
