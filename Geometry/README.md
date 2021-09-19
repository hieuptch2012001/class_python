1 - Write a Geometry class with default constructor having no parameters.

    class Geometry():
        def __init__(self):
            pass

2 - Write a methode in Geometry class called distance() that allow to compute a distance between two points A = (a1, a2), B = (b1, b2) (with the convention: a point M is identified with its pair of coordinates M = ( x, y)).

    from math import sqrt
    from math import pow

    def distance(self, x1, y1, x2, y2):
        return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) * 1.0)

3 - Write a methode in Geometry class called middle() allowing to determine the midle of bipoint (A,B).

    def middle(self, x1, y1, x2, y2):
        a = (x1 + x2) / 2
        b = (y1 + y2) / 2
        print(f"midpoint: (", a, ",", b, ")")

4 - Write method called trianglePerimeter() allowing to compute the perimeter of triangle

    def checkTriangle(self, a, b, c):
        if (a + b > c and a + c > b and b + c > a):
            return True
        else:
            return False

    def trianglePerimeter(self, a, b, c):
        if self.checkTriangle(a, b, c) == True:
            return a + b + c
        else:
            return False

5 - Write method called triangleIsoscel() which returns a True if the triangle is isoscel and False if not.

    def trianglelsoscel(self, a, b, c):
        if self.checkTriangle(a, b, c) == True:
            if (a == b != c or a == c != b or b == c != a):
                print("True trianglelsoscel\n")
            else:
                print("False trianglelsoscel\n")
        else:
            print("no triangle")
