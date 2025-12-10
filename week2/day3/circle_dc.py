#Daily Challenge - Circle
#The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

import math

class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    # --------- Alternate constructor using a decorator ---------
    @classmethod
    def from_diameter(cls, diameter: float):
        """Create a Circle using the diameter."""
        if diameter <= 0:
            raise ValueError("Diameter must be positive.")
        return cls(diameter / 2)

    # --------- Properties ---------
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter must be positive.")
        self.radius = value / 2

    # --------- Area ---------
    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    # --------- Representation ---------
    def __repr__(self):
        return f"Circle(radius={self.radius})"

    # --------- Addition ---------
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)

    # --------- Comparisons ---------
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __lt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius


c1 = Circle(5)

c2 = Circle.from_diameter(20)
print(c2.radius)   # 10

print(c1.radius)
print(c1.diameter)

c1.diameter = 50
print(c1.radius)   # 25

print(c1.area)
print(c1)  # Circle(radius=25)

c3 = c1 + c2
print(c3)   # New circle with combined radius
print(c1 == c2)  # False
print(c1 > c2)   # True
print(c1 < c2)   # False

print(c1 > c2)
print(c1 == c2)
# Example usage:
c1 = Circle(5)
c2 = Circle.from_diameter(20)
print(c2.radius)   # 10

circles = [Circle(10), Circle(3), Circle(7)]
circles.sort()
print(circles)
# Output: [Circle(radius=3), Circle(radius=7), Circle(radius=10)]
