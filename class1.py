import math

# Get input from the user
a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

# Check if the sides form a valid triangle
if a + b > c and a + c > b and b + c > a:
    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculating the area using Heron's formula
    a2 = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(a2)
    print("Area is ->", area)
    print("----------------------------------")
    
    # Calculate the perimeter
    print("Perimeter is ->", a + b + c)
    print("----------------------------------")
    
    # Calculate the angles in radians using the sine rule
    angle1_rad = math.asin((2 * area) / (b * c))
    angle2_rad = math.asin((2 * area) / (a * c))
    angle3_rad = math.asin((2 * area) / (a * b))

    # Convert angles from radians to degrees
    angle1_deg = math.degrees(angle1_rad)
    angle2_deg = math.degrees(angle2_rad)
    angle3_deg = math.degrees(angle3_rad)

    print("Angle1 ->", angle1_deg, "degrees")
    print("Angle2 ->", angle2_deg, "degrees")
    print("Angle3 ->", angle3_deg, "degrees")
else:
    print("The entered sides do not form a valid triangle.")
    print("----------------------------------")

# Convert Celsius to Fahrenheit
cel = float(input("Enter the temperature in Celsius: "))
print("Temperature in Fahrenheit is ->", 1.8 * cel + 32)
print("----------------------------------")

# Convert Fahrenheit to Celsius
f = float(input("Enter the temperature in Fahrenheit: "))
print("Temperature in Celsius is ->", (5/9) * (f - 32))
print("----------------------------------")
