import math

# ----- Point Class -----
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # equality check
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # string representation
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # distance between two points
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# ----- Vector Class (inherits Point) -----
class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    # vector addition
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


# ----- Testing the classes -----
if __name__ == "__main__":
    # Points
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    print(p1)                    # Point(2, 3)
    print(p2)                    # Point(5, 7)
    print("Equal:", p1 == p2)    # False
    print("Distance:", p1.distance(p2))  # e.g. 5.0

    # Vectors
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1)                    # Vector<1, 2>
    print(v2)                    # Vector<3, 4>
    print("Vector sum:", v1 + v2)  # Vector<4, 6>
