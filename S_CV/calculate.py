class numerals():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def sum(self):
        return self.number1 + self.number2

    def sub(self):
        return self.number1 - self.number2

    def mul(self):
        return self.number1 * self.number2

    def div(self):
        return self.number1 / self.number2


def main():
    a = float(input("Nhập a = "))
    b = float(input("Nhập b = "))
    nub = numerals(a, b)

    print("a + b = ", nub.sum())
    print("a - b = ", nub.sub())
    print("a * b = ", nub.mul())
    print("a / b = ", nub.div())


if __name__ == '__main__':
    main()
