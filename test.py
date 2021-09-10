class Computation:
    def __init__(self):
        pass
# --- Factorial ------------

    def factorial(self, n):
        j = 1
        for i in range(1, n + 1):
            j = j * i
        return j

# --- Sum of the first n numbers ----
    def sum(self, n):
        j = 1
        for i in range(1, n + 1):
            j = j + i
        return j

# --- Primality test of a number ------------
    def testPrim(self, n):
        j = 0
        for i in range(1, n + 1):
            if (n % i == 0):
                j = j + 1
        if (j == 2):
            return True
        else:
            return False

# --- Primality test of two integers ------------
    def testprims(self, n, m):

        # initialize the number of commons divisors
        commonDiv = 0
        for i in range(1, n + 1):
            if (n % i == 0 and m % i == 0):
                commonDiv = commonDiv + 1
        if commonDiv == 1:
            print("The numbers", n, "and", m, "are co-primes")
        else:
            print("The numbers", n, "and", m, "are not co-primes")

# ---Multiplication table-------------
    def tableMult(self, k):
        for i in range(1, 10):
            print(i, "x", k, "=", i * k)

# --- All multiplication tables of the numbers 1, 2, .., 9
    def allTables(self):
        for k in range(1, 10):
            print("\nthe multiplication table of:", k, "is:")
            for i in range(1, 10):
                print(i, "x", k, "=", i * k)

# ----- list of divisors of an integer
    def listDiv(self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range(1, n + 1):
            if (n % i == 0):
                lDiv.append(i)
        return lDiv

# ------ list of prime divisors of an integer ----------------
    def listDivPrim(self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range(1, n + 1):
            if (n % i == 0 and self.testPrim(i)):
                lDiv.append(i)
        return lDiv


# Instantiation example
Comput = Computation()
Comput.testprims(13, 7)
print(Comput.factorial(9))
print("List of divisors of 18:", Comput.listDiv(18))
print("List of prime divisors of 18:", Comput.listDivPrim(18))
Comput.allTables()
