print("Strings in Python: ")
print("Strings are immutable in Python.")

name = "Shashank Dubey"

print("Select char from 0 to 5: ", name[0:5])  # Select char from 0 to 5
print("Select char from 0 to 5 with step 2: ", name[0:5:2])  # Select char from 0 to 5 with step 2
print("Select char from start to 5: ", name[:5])  # Select char
print("Select char from 5 to end: ", name[5:])  # Select char
print("Select char from start to end with step 3: ", name[::3])  # Select char from start to end with step 3
print("Select char from end to start: ", name[::-1])  # Select char from

# Ecoding and Decoding
encoded_name = name.encode("utf-8")
print("Encoded name: ", encoded_name)
print("Decoded name: ", encoded_name.decode("utf-8"))