for i in range(0,11,2):
    print(i)

list = []
for i in range(1,11):
    temp = []
    for j in range(1, 11):
        temp.append(f"{i} x {j} = {i*j}")
    list.append(temp)

# print(list)

# Ennumerate
tech_stacks = ["Reactjs", "Nodejs", "Nestjs"]

for index, tech_stack in enumerate(tech_stacks):
    print(index, " - ", tech_stack)


# zip

for name in zip(["Shashank", "Vishal"],[1000, 2000]):
    print(name)

# Break, Continue and loop fallback