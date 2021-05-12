class numerals():
    number1 = 0
    number2 = 0

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        print('a + b = ', self.number1 + self.number2)

    def sub(self):
        print('a - b = ', self.number1 - self.number2)

    def mul(self):
        print('a * b = ', self.number1 * self.number2)

    def div(self):
        if self.number2 != 0:
            print('a / b = ', self.number1 / self.number2)
        else:
            print("erorr")


def main():

    nub = numerals(5, 3)

    print(nub.sum())
    print(nub.sub())
    print(nub.mul())
    print(nub.div())


if __name__ == '__main__':
    main()
