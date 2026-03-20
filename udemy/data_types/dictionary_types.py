from rich import print
from rich.pretty import Pretty
print("Dictionary in python")

tech_stacks = {
    "backend": ["Python", "Django", "Flask"],
    "frontend": ["JavaScript", "React", "Vue.js"],
    "database": ["PostgreSQL", "MongoDB", "MySQL"]
}

print(Pretty(tech_stacks))

print("Backend list - ",tech_stacks["backend"])

print("Frontend list - ",tech_stacks.get("frontend"))

# Adding a new key-value pair
tech_stacks["devops"] = ["Docker", "Kubernetes", "AWS"]

print("After adding DevOps:", tech_stacks)

# Updating an existing key-value pair
tech_stacks["backend"].append("FastAPI")

print("After updating Backend:", tech_stacks)

# Removing a key-value pair
removed_value = tech_stacks.pop("database", None)

print("Removed Database value:", removed_value)
print("After removing Database:", tech_stacks)

# Remove the last inserted key-value pair (Python 3.7+)
last_item = tech_stacks.popitem()
print("Removed last item:", last_item)
print("After popitem:", tech_stacks)

# Check if a key exists
print("Is 'frontend' in tech_stacks?", "frontend" in tech_stacks)

# Iterate through keys and values
for key, value in tech_stacks.items():
    print(f"{key}: {value}")    

# Clear the dictionary
# tech_stacks.clear() 
# print("After clearing:", tech_stacks)

# Nested dictionary
company_tech = {
    "CompanyA": {
        "backend": ["Python", "Django"],
        "frontend": ["JavaScript", "React"]
    },
    "CompanyB": {
        "backend": ["Java", "Spring"],
        "frontend": ["JavaScript", "Angular"]
    }
}

print("Company Tech Stacks:", Pretty(company_tech))
print("Keys in company_tech:", list(company_tech.keys()))
print("Values in company_tech:", Pretty(company_tech.values()))

# Merging two dictionaries
additional_tech = { "mobile": ["Flutter", "React Native"] }
tech_stacks.update(additional_tech)     
print("After merging additional tech:", Pretty(tech_stacks))

# Dictionary comprehension

squared_numbers = {x: x*x for x in range(5,10)}
print("Squared Numbers:", squared_numbers)

# Check if key exists
print("Is 'devops' in tech_stacks?", "devops" in tech_stacks)

# Check if value exists
print(tech_stacks)
print("Is ['Python', 'Django', 'Flask'] in tech_stacks?", ["Python", "Django","Flask"] in tech_stacks.values())


ai_startups = {
    "StartupA": {  "AI": ["NLP", "Computer Vision"], "Cloud": ["AWS", "Azure"]},
    "StartupB": {  "AI": ["Reinforcement Learning", "GANs"], "Cloud": ["GCP", "AWS"]}
}

print(ai_startups.keys())
print(ai_startups.values())
print(ai_startups.items())


