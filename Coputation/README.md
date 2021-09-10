1 - Create a Coputation class with a default constructor (without parameters) allowing to perform various calculations on integers numbers.\

    class Coputation():
        def __init__(self):
            pass

2 - Create a method called Factorial() which allows to calculate the factorial of an integer. Test the method by instantiating the class.

    def Factorial(self, n):
        if n == 1:
            return 1
        else:
            return (n * self.Factorial(n-1))

3 - Create a method called Sum() allowing to calculate the sum of the first n integers 1 + 2 + 3 + .. + n. Test this method.

    def Sum(self, n):
        a = 1
        for i in range(1, n + 1):
            a = a + i
        return a

4 - Create a method called testPrim() in the Calculation class to test the primality of a given integer. Test this method.

    def testPrim(self, n):
        j = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False

5 - Create a method called testPrims() allowing to test if two numbers are prime between them.

    def testPrims(self, n, m):
        div = 0
        for i in range(1, n + 1):
            if (n % i == 0 and m % i == 0):
                div = div + 1
        if div == 1:
            print("There are two prime numbers")
        else:
            print("There are no two primes")

6 - Create a tableMult() method which creates and displays the multiplication table of a given integer. Then create an allTablesMult() method to display all the integer multiplication tables 1, 2, 3, ..., 9.

    def tableMult(self, mul):
        for i in range(1, 10):
            print(i, "x", mul, "=", i * mul)

    def allTablesMult(self):
        for i in range(1, 10):
            print("\nMultiplication table", i)
            for j in range(1, 11):
                print(i, "x", j, "=", i * j)

7 - Create a static listDiv() method that gets all the divisors of a given integer on new list called Ldiv. Create another listDivPrim() method that gets all the prime divisors of a given integer.

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
