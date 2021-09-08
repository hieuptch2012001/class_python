#Create a Python class Person with attributes: name and age of type string.

    class Person():
        def __init__(self, name, age):
            self.name = name
            self.age = age

#Create a display() method that displays the name and age of an object created via the Person class.

    def Display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

#Create a child class Student which inherits from the Person class and which also has a section attribute.

    class Student(Person):
        def __init__(self, name, age, section):
            super().__init__(name, age)
            self.section = section

#Create a method displayStudent() that displays the name, age and section of an object created via the Student class.

    def displayStudent(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Section : ", self.section)

#Create a student object via an instantiation on the Student class and then test the displayStudent method.

    myStudent = Student("lorem 2", "20", "lorem ipsum")
    myStudent.displayStudent()
