#Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.

    class Rectangle():
        def __init__(self, length, width):
            self.length = length
            self.width = width

#Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of ​​the rectangle.

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

#Create a method display() that display the length, width, perimeter and area of an object created using an instantiation on rectangle class.

    def Display(self):
        print("length = ", self.length)
        print("width = ", self.width)
        print("perimeter = ", self.Perimeter())
        print("area = ", self.Area())

#Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

    class Parallelepipede(Rectangle):
        def __init__(self, length, width, height):
            Rectangle.__init__(self, length, width)
            self.height = height

        def Volume(self):
            return self.length * self.width * self.height
