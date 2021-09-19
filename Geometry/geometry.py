from math import sqrt
from math import pow


class Geometry():
    def __init__(self):
        pass

    def distance(self, x1, y1, x2, y2):
        return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) * 1.0)

    def middle(self, x1, y1, x2, y2):
        a = (x1 + x2) / 2
        b = (y1 + y2) / 2
        print(f"midpoint: (", a, ",", b, ")")

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

    def trianglelsoscel(self, a, b, c):
        if self.checkTriangle(a, b, c) == True:
            if (a == b != c or a == c != b or b == c != a):
                print("True trianglelsoscel\n")
            else:
                print("False trianglelsoscel\n")
        else:
            print("no triangle")


def main():
    geo = Geometry()

    print("\nDistance between 2 points A = (2, 3) , B = (5, 7) is %.6f" %
          (geo.distance(2, 3, 5, 7)))
    print("\n*********\n")

    geo.middle(2, 3, 5, 7)
    print("\n*********\n")

    print("Perimeter of triangle is", geo.trianglePerimeter(2, 3, 4))
    print("\n*********\n")

    geo.trianglelsoscel(7, 7, 5)


if __name__ == '__main__':
    main()
