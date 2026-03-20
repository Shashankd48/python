print("List Data Type in Python")

tech_stacks = ["Python", "Django", "JavaScript", "React", "Node.js",["HTML", "CSS",["Bootstrap", "Tailwind",]]]

# printing the list
print(tech_stacks)

# checking membership
print(f"Is Python in tech_stacks? {'Python' in tech_stacks}")

# iterating through a list
for tech in tech_stacks:    
    print(tech)

# appending an element
tech_stacks.append("Flask")
print(tech_stacks)

# removing an element
tech_stacks.remove("Node.js") 
print(tech_stacks)

# extending a list with another list
tech_stacks.extend(["GraphQL", "TypeScript"])       
print(tech_stacks)

# inserting an element at a specific index
tech_stacks.insert(1, "FastAPI")    
print(tech_stacks)

# popping an element by index
popped_tech = tech_stacks.pop(1)    
print(f"Popped technology: {popped_tech}")
print(tech_stacks)

# reversing the list
tech_stacks.reverse()   
print(tech_stacks)

# sorting the list (only works if all elements are of the same type)
numeric_list = [5, 2, 9, 1, 5, 6]
numeric_list.sort()

print(numeric_list)

# minimum and maximum
print(f"Minimum: {min(numeric_list)}")
print(f"Maximum: {max(numeric_list)}")  

# Sorting tech_stacks will raise an error because it contains mixed data types
tech_stacks.sort()  # Uncommenting this line will raise a TypeError   
print(tech_stacks)
