import math

# ---------- Point Class ----------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Equality check
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    # String representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Euclidean distance to another point
    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("distance_to expects a Point object")
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


# ---------- Vector Class ----------
class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    # Override string representation
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Override + operator for vector addition
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)


# ---------- Demonstration ----------
if __name__ == "__main__":
    # Create Points
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    print(p1)                  # Point(1, 2)
    print(p2)                  # Point(4, 6)
    print("Equal?", p1 == p2)  # False
    print("Distance:", p1.distance_to(p2))  # 5.0

    # Create Vectors
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1)                  # Vector(1, 2)
    print(v2)                  # Vector(3, 4)

    # Vector addition
    v3 = v1 + v2
    print("v1 + v2 =", v3)     # Vector(4, 6)

    # Check equality
    v4 = Vector(4, 6)
    print("v3 == v4?", v3 == v4)  # True

    # Distance between vectors (inherited from Point)
    print("Distance v1 -> v2:", v1.distance_to(v2))  # 2.82