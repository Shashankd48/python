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