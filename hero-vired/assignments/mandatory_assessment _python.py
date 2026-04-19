# Question 1: ATM Withdrawal System 
# Write a Python program that simulates an ATM withdrawal system. The program should validate the withdrawal request based on multiple conditions before processing it.

current_balance = 5000  # Example balance

# Return False

def atm_withdrawal(withdrawal_amount):
    
    # Validation 1: Withdrawal amount must be greater than 0
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False
    
    # Validation 2: Withdrawal amount must be a multiple of 500
    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be multiple of 500")
        return False
    
    # Validation 3: Account balance must be sufficient for withdrawal
    if withdrawal_amount > current_balance:
        print(f"Error: Insufficient balance. Available: ${current_balance}")
        return False
    
    # If all validations pass:
    remaining_balance = current_balance - withdrawal_amount
    print(f"Withdrawal successful. Amount: ${withdrawal_amount}")
    print(f"Remaining balance: ${remaining_balance}")
    return True

withdrawal_amount = int(input("Enter the withdrawal amount: "))
atm_withdrawal(withdrawal_amount)

# Question 2: Restaurant Bill Calculator
# Write a Python program that calculates the total restaurant bill including service charge, tax, and tip.

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

# Question 3: Login Authentication System (10 Marks)
# Write a Python program that validates a user's login credentials based on specific security requirements.

def validate_login(username, password):
    # Validation 1: Username length must be at least 5 characters
    if len(username) < 5:
        print("Error: Username must be at least 5 characters")
        return False
    
    # Validation 2: Password length must be at least 8 characters
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
        return False
    
    # Validation 3: Password must contain at least one digit (0-9)
    if not any(char.isdigit() for char in password):
        print("Error: Password must contain at least one digit")
        return False
    
    # If all validations pass:
    print("Login successful")
    return True

username = input("Enter username: ")
password = input("Enter password: ")
validate_login(username, password)