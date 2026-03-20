tech_stacks = ["Python", "Django", "JavaScript", "React", "Node.js"]
frontend_stacks = ["HTML", "CSS", "JavaScript", "React", "Vue.js"]

print(tech_stacks * 2)  # Repetition
print(tech_stacks + frontend_stacks)  # Concatenation

# handler error in try / catch
try:
    print(tech_stacks - ["Django"])  # Subtraction (will raise an error)
except TypeError as e:
    print(f"Error: {e}")

try:
    print(tech_stacks / 2)  # Division (will raise an error)
except TypeError as e:
    print(f"Error: {e}")

# example of bytearray
database = bytearray(b"User data in bytes")
print(database)
print(database.replace(b"User", b"Admin"))

