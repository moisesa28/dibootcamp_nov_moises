#Daily Challenge - Circle
#The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if (radius is not None and diameter is not None) or (radius is None and diameter is None):
            raise ValueError("Provide either radius or diameter, but not both or neither.")

        if radius is not None:
            self.radius = radius # This will call the setter
        elif diameter is not None:
            self.diameter = diameter # This will call the setter

        def __repr__(self):
        return f"Circle(radius={self.radius})"

        def __add__(self):
            


# Example Usage and Verification:
print("--- Initializing Circles ---")
circle1 = Circle(radius=5)
print(f"Circle 1: {circle1}, Radius: {circle1.radius}, Diameter: {circle1.diameter}")

circle2 = Circle(diameter=10)
print(f"Circle 2: {circle2}, Radius: {circle2.radius}, Diameter: {circle2.diameter}")

# Test property setters
print("\n--- Testing Setters ---")
circle1.radius = 7
print(f"Circle 1 (radius set to 7): {circle1}, Radius: {circle1.radius}, Diameter: {circle1.diameter}")

circle2.diameter = 14
print(f"Circle 2 (diameter set to 14): {circle2}, Radius: {circle2.radius}, Diameter: {circle2.diameter}")

# Test ValueErrors
print("\n--- Testing ValueErrors ---")
try:
    Circle(radius=5, diameter=10)
except ValueError as e:
    print(f"Error: {e}")

try:
    Circle()
except ValueError as e:
    print(f"Error: {e}")

try:
    circle1.radius = -2
except ValueError as e:
    print(f"Error: {e}")

try:
    circle2.diameter = -5
except ValueError as e:
    print(f"Error: {e}")


