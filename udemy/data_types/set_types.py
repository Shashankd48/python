print("Set in python")

tech_stacks = {"Python", "Django", "JavaScript", "React", "Node.js"}

frontend_tech_stacks = {"JavaScript", "React", "Vue.js", "Angular"}

print("All Tech Stacks:", tech_stacks | frontend_tech_stacks) # Union

print("Common Tech Stacks:", tech_stacks & frontend_tech_stacks) # Intersection

print("Tech Stacks in tech_stacks but not in frontend_tech_stacks:", tech_stacks - frontend_tech_stacks) # Difference

print("Tech Stacks in either tech_stacks or frontend_tech_stacks but not both:", tech_stacks ^ frontend_tech_stacks) # Symmetric Difference

print("Is 'Python' in tech_stacks?", "Python" in tech_stacks)

tech_stacks.add("Flask")
print("After adding Flask:", tech_stacks)


branch_a_products = {"bread","milk","butter","jam"}

branch_b_products = {"bread","cheese","butter","ketchup"}

print(branch_a_products)
print(branch_b_products)

print(branch_a_products & branch_b_products)

print(branch_a_products | branch_b_products)

print(branch_a_products - branch_b_products)

print("ketchup" in branch_a_products)

essential_items = {"milk","bread","ketchup"}

print(essential_items)

# Return unique items from both sets
print(essential_items ^ branch_a_products) # Symmetric Difference

# using methods
print(essential_items.union(branch_b_products)) 
