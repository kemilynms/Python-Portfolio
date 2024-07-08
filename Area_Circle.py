import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area

# Example usage:
radius = 5
area = calculate_circle_area(radius)
print(f"Area of a circle with radius {radius} is: {area:.2f}")
