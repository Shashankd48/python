def calculate_restaurant_bill(meal_cost):
    # Calculate service charge
    service_charge = 0.10 * meal_cost
    
    # Calculate amount after service
    amount_after_service = meal_cost + service_charge
    
    # Calculate tax
    tax = 0.05 * amount_after_service
    
    # Calculate tip
    tip = 0.05 * amount_after_service
    
    # Calculate total bill
    total_bill = amount_after_service + tax + tip
    
    print(f"Meal Cost: {meal_cost:.2f}")
    print(f"Service Charge (10%): {service_charge:.2f}")
    print(f"Amount after Service: {amount_after_service:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Tip (5%): {tip:.2f}")
    print(f"Total Bill: {total_bill:.2f}")

    return total_bill

meal_cost = float(input("Enter the meal cost: "))
calculate_restaurant_bill(meal_cost)