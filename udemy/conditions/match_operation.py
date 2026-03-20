# Tran reservation system

seat_type = input("Enter seat type (Sleper/AC/General/Luxury): ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC - available")
    case "ac":
        print("AC not available")
    case "general":
        print("Lowest price")
    case "luxury":
        print ("Ac with free meal")
    case _:
        print("Invalid seat type")