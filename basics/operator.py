
item1 = 42
item2 = 42
item3 = "Hello, world!"

print (str(item1)+ str(item2)+ " " + item3)

# print("username: \t",)
# username = input()

# print("password: ")
# password = input()

# print("Your credentials: ", username, password)

value = int(input())

def isEven(value):
    return True if value % 2 == 0 else False

def printEvenOdd(value):
    return "Even" if value % 2 == 0 else "Odd"

if value < 10:
    print("Your value is too low 😨")
    print("You value is", printEvenOdd(value))
elif value == 10 :
    print("Your value is perfect 😊")
else: 
    print("Your value is too high 🙄")

for i in range(10000000):
    print(i)

