class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2*(self.length + self.width)

    def Area(self):
        return self.length * self.width

    def Display(self):
        print("length = ", self.length)
        print("width = ", self.width)
        print("perimeter = ", self.Perimeter())
        print("area = ", self.Area())


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self, length, width)
        self.height = height

    def Volume(self):
        return self.length * self.width * self.height


def main():
    length = int(input("Length = "))
    width = int(input("Width = "))
    height = int(input("Height = "))
    print("\n************\n")

    rectangle = Rectangle(length, width)
    rectangle.Display()

    print("\n************\n")

    paralle = Parallelepipede(length, width, height)
    print("Volume = ", paralle.Volume())


if __name__ == '__main__':
    main()
