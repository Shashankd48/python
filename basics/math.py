import math

pie = 3.14
print(math.floor(pie))

print(math.ceil(pie))

print(math.cos(pie))

def areaOfSquare(side):
    return side*side

def areaOfCircle(radius):
    return  math.pi * radius * radius

print("Area of square",areaOfSquare(2))

print("Area of circle",areaOfCircle(10))

print(type(pie))

print("4" - "6")