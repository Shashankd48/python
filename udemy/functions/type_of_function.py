# Types of functions in Python

# 1. Built-in functions: These are functions that are pre-defined in Python and can be used without any additional code. Examples include print(), len(), and input().

# 2. User-defined functions: These are functions that are created by the user to perform specific tasks. They are defined using the def keyword and can take parameters and return values.

# 3. Lambda functions: These are anonymous functions that are defined using the lambda keyword. They are typically used for short, simple functions that can be defined in a single line of code.

# 4 Pure functions: These are functions that always produce the same output for the same input and have no side effects. They do not modify any external state and do not rely on any external state.

# 5. Higher-order functions: These are functions that can take other functions as arguments or return functions as their result. They are often used in functional programming to create more flexible and reusable code.


# Impure function example

def add_to_list(lst, item):
    lst.append(item)
    return lst  

my_list = [1, 2, 3]
print(add_to_list(my_list, 4))  # Output: [1, 2, 3, 4]
print(my_list)  # Output: [1, 2, 3, 4] - the original list is modified, showing that this function has side effects and is not pure.

counter = 1

def impure_increment():
    global counter
    counter +=1
    return counter

print(impure_increment())  # Output: 2

# Pure function example
def add(a, b):
    return a + b
print(add(5, 3))  # Output: 8
print(add(5, 3))  # Output: 8 - the same output for the same input, and no side effects, making this a pure function.

# Higher-order function example
def apply_operation(a, b, operation):
    return operation(a, b)

# Example usage
print(apply_operation(5, 3, add))  # Output: 8  

# Recursive function example
def factorial(n):
    """This function calculates the factorial of a given number n using recursion.
    :param n: The number for which to calculate the factorial.
    :return: The factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120

# Lambda function example
square = lambda x: x * x
print(square(4))  # Output: 16

# Lambda function with multiple arguments
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8

# Lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# Built-in function example
def chai_flavor(flavor):
    """This function takes a flavor as input and returns a string describing the chai flavor.
    """
    print(f"Your chai flavor is: {flavor}")

print(chai_flavor.__doc__)  # Output: This function takes a flavor as input and returns a string describing the chai flavor.
print(chai_flavor.__name__)  # Output: chai_flavor
chai_flavor("Masala")  # Output: Your chai flavor is: Masala

help(chai_flavor)  # This will display the docstring and other information about the function.

print(2 * 2)

