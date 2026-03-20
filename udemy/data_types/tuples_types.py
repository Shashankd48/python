tech_stacks = ("Python", "Django", "JavaScript", "React", "Node.js")


print(tech_stacks)
print(f"Is Python in tech_stacks? {'Python' in tech_stacks}")

# iterating through a tuple
for tech in tech_stacks:
    print(tech)

# accessing elements by index
print(tech_stacks[0])  # First element

# swapping values using tuple unpacking
a = 5 
b = 10
a, b = b, a     
print(a, b)  # Output: 10 5     