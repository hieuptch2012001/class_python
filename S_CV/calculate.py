class numerals():
    __number1 = 0
    __number2 = 0

    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def sum(self):
        return self.__number1 + self.__number2

    def sub(self):
        return self.__number1 - self.__number2

    def mul(self):
        return self.__number1 * self.__number2

    def div(self):
        if self.__number2 != 0:
            return self.__number1 / self.__number2
        else:
            print("erorr")


def main():

    nub = numerals(6, 2)

    print('a = ', nub._numerals__number1)
    print('b = ', nub._numerals__number2)

    print("----------------")

    print('a + b = ', nub.sum())
    print('a - b = ', nub.sub())
    print('a * b = ', nub.mul())
    print('a / b = ', nub.div())


if __name__ == '__main__':
    main()
