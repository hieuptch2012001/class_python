class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Display(self):
        print("Name : ", self.name)
        print("Age : ", self.age)


class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Section : ", self.section)


def main():
    myPerson = Person("lorem 1", "22")
    myPerson.Display()
    print("\n***********\n")

    myStudent = Student("lorem 2", "20", "lorem ipsum")
    myStudent.displayStudent()


if __name__ == "__main__":
    main()
