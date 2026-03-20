print("Commond line inputs")

tech_stack = input("Your favorite tech stack - ")
experience = input("Years of experience - ")

print(tech_stack)
print(int(experience) + 10)

def calculate_delivery_charge(distance: float) -> str:
    # Write your code below this line
    distance = float(input("distance in kilometers"))
    
    if distance <= 2:
        return "Delivery charge: 0"
    elif distance > 2 and distance <= 5:
        return "Delivery charge: 30"
    elif distance > 5 and distance <= 10:
        return "Delivery charge: 50"
    else:
        return "Delivery not available for your location."
    
    pass