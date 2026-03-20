def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Green", "Yes","Low")

make_chai(milk="No",sugar="High", tea="Darjeeling")

# *args and *kwargs - key:word arguments

def special_chai(*ingredients, **extras):
    print(ingredients)
    print(extras)

special_chai("Lemon","Water", sugar=10, cream="No")

def generate_invoice(customer_name: str = "Guest", *items: str, **charges: float) -> str:
    print("# Output")
    print(f"# Invoice for {customer_name}:")
    
    total = 0

    if items:
        print("# Items:")
        for item in items:
            print(f"# - {item}")

    if charges:
        print("# Charges:")
        for key, amount in charges.items():
            print(f"# {key.capitalize()}: {amount}")
            total += amount

    print("# Total Amount Due:", total)
    print()  # blank line for readability


generate_invoice("Amit", "Burger", "Fries", tax=50.0, service=20.0)

generate_invoice()

generate_invoice("John",)