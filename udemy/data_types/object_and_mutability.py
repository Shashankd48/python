import sys

print("Object Data Type in Python")

print("In Python, everything is an object. This includes data types like integers, strings, lists, and even functions and classes.\n\n")

name = "Shashank"

name = "Vishal"

print(f"id of name: {id("Shanshank")}")

print(f"id of name: {id(name)}")

print("\n\nMutability:")

tech_stack = set({})

tech_stack.add("Python")
tech_stack.add("JavaScript")
tech_stack.add("C++")   

print(f"Tech Stack: {tech_stack}")

# Other data types

integer_var = 10
float_var = 10.5
string_var = "Hello, World!"
list_var = [1, 2, 3, 4, 5]
tuple_var = (1, 2, 3)   
dict_var = {"name": "Alice", "age": 30}
set_var = {1, 2, 3, 4, 5,}
bool_var = True
none_var = None
complex_var = 2 + 3j
range_var = range(10)
bytes_var = b"Hello"
bytearray_var = bytearray(b"Hello")
memoryview_var = memoryview(b"Hello")
frozenset_var = frozenset({1, 2, 3})
function_var = lambda x: x * 2
class_var = type("MyClass", (object,), {})

print(function_var(5))  # Output: 10

print("Modular example:", 10 % 3)  # Output: 1

print("Exponent example:", 2 ** 3)  # Output: 8

print("Floor Division example:", 10 // 3)  # Output: 3

print(dict_var["name"])

print(set_var)

water_hot = True
tea_added = False

if(water_hot and tea_added):
    print("Tea is ready!")
else:
    print("Tea is not ready yet.")


print(sys.float_info)

print(bytes_var)