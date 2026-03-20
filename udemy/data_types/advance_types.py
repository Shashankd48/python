print("Advanced Data Types in Python")

# List - Mutable Ordered Collection
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.insert(0, 0)
print("List:", my_list)

# Tuple - Immutable Ordered Collection
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Set - Unordered Collection of Unique Elements - Mutable
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)


# Dictionary - Key-Value Pairs - Mutable
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Dictionary:", my_dict)

# Frozenset - Immutable Set - Unordered Collection of Unique Elements
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", my_frozenset)

# Demonstrating Mutability
my_list.append(6)
print("Modified List:", my_list)

# Datetime - Date and Time Representation
from datetime import datetime
now = datetime.now()
print("Current Date and Time:", now)

# Date - Date Representation
from datetime import date
today = date.today()
print("Today's Date:", today)

# Time - Time Representation
from datetime import time
current_time = time(14, 30, 0)
print("Current Time:", current_time)

# Complex Number - Real and Imaginary Parts
my_complex = 3 + 4j
print("Complex Number:", my_complex)
print("Real Part:", my_complex.real)
print("Imaginary Part:", my_complex.imag)
print("Magnitude:", abs(my_complex))

print("\n**Using Collections Module**\n")

# Collections Module - Specialized Data Structures
from collections import namedtuple, deque, Counter, OrderedDict, defaultdict

# Named Tuple - Immutable and Lightweight Object Type
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)

print("\nNamed Tuple Point:", p)

# Deque - Double-Ended Queue - Mutable
my_deque = deque([1, 2, 3])
my_deque.appendleft(0)
my_deque.append(4)
print("\nDeque:", my_deque)
my_deque.pop()
my_deque.popleft()
print("\nModified Deque:", my_deque)

# Counter - Count Hashable Objects - Mutable
my_counter = Counter(['a', 'b', 'c', 'a', 'b', 'a'])
print("\nCounter:", my_counter)
print("Most Common Elements:", my_counter.most_common(2))
my_counter.update(['b', 'c', 'c','d'])
print("Updated Counter:", my_counter)

# OrderedDict - Dictionary that Maintains Insertion Order - Mutable
my_ordered_dict = OrderedDict()
my_ordered_dict['a'] = 1
my_ordered_dict['b'] = 2
my_ordered_dict['c'] = 3
print("\nOrderedDict:", my_ordered_dict)
my_ordered_dict.move_to_end('b')
print("Modified OrderedDict:", my_ordered_dict)

# DefaultDict - Dictionary with Default Values for Missing Keys - Mutable
my_default_dict = defaultdict(int)
my_default_dict['a'] += 1
my_default_dict['b'] += 2
print("\nDefaultDict:", my_default_dict)
print("Accessing Missing Key 'c':", my_default_dict['c'])  # Returns 0 by default

# adding string to DefaultDict
# my_default_dict["c"] += "hello"
# print("After adding string to key 'c':", my_default_dict) # Gives error unsupported

# Note: defaultdict with int as default factory cannot concatenate strings directly.    

# To handle both integers and strings, we can use a custom default factory.
def custom_default():
    return ""
my_custom_default_dict = defaultdict(custom_default)
my_custom_default_dict['a'] += "hello"
my_custom_default_dict['b'] += " world"
print("Custom DefaultDict with strings:", my_custom_default_dict)


# This will now work without error.
print("\n**End of Advanced Data Types Demonstration**")

