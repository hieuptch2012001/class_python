class Coputation():
    def __init__(self):
        pass

    def Factorial(self, n):
        if n == 1:
            return 1
        else:
            return (n * self.Factorial(n-1))

    def Sum(self, n):
        # a = 0
        # for i in range(1, n + 1):
        #     a = a + i
        a = n * ((n + 1) / 2)
        return a

    def testPrim(self, n):
        j = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False

    def testPrims(self, n, m):
        div = 0
        for i in range(1, n + 1):
            if (n % i == 0 and m % i == 0):
                div = div + 1
        if div == 1:
            print("There are two prime numbers")
        else:
            print("There are no two primes")

    def tableMult(self, mul):
        for i in range(1, 10):
            print(i, "x", mul, "=", i * mul)

    def allTablesMult(self):
        for i in range(1, 10):
            print("\nMultiplication table", i)
            for j in range(1, 11):
                print(i, "x", j, "=", i * j)

    def listDiv(self, n):
        print("List of divisors of ", n)
        for i in range(1, n + 1):
            if (n % i == 0):
                print(i, end=", ")

    def listDivPrim(self, n):
        lis = []
        for i in range(1, n + 1):
            if (n % i == 0 and self.testPrim(i)):
                lis.append(i)
        return lis


def main():
    cop = Coputation()

    print("\nThe factorial of 9 is", cop.Factorial(9))
    print("\n*********\n")

    print("sum of numbers 20 (1 + 2 + ... + 20) =", cop.Sum(20))
    print("\n*********\n")

    cop.testPrim(7)
    print("\n*********\n")

    cop.testPrims(3, 10)
    print("\n*********\n")

    cop.tableMult(9)
    print("\n*********")

    cop.allTablesMult()
    print("\n*********\n")

    print("List of prime divisors of 99:", cop.listDivPrim(99), "\n")

    # cop.listDivPrim(99)


if __name__ == '__main__':
    main()
