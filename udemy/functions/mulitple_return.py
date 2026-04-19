def make_chai():
    return "Chai is ready!", "Enjoy your drink!"

def test():
    print("Testing multiple return values:")

value = make_chai()
testValue = test()
print(testValue)  # This will print None since test() does not return anything
print(value)

# Mulitple value return

def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result

# sum_result, product_result = calculate(5, 3)
sum_result, product_result = calculate(5, 3)
print("Sum:", sum_result)  # Accessing the sum result