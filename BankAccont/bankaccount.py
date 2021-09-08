class BankAccount():
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def Deposit(self, sum):
        self.balance = self.balance + sum

    def Withdrawal(self, sub):
        if self.balance < sub:
            print("Out of money\n")
        else:
            self.balance = self.balance - sub

    def bankFees(self):
        self.balance = self.balance - (self.balance * 0.5)

    def display(self):
        print("Name : ", self.name)
        print("AccountNumber : ", self.accountNumber)
        print("Balance : ", self.balance)
        print("\n")


def main():
    name = input("Name = ")
    accountNumber = int(input("Account Number = "))
    balance = int(input("Balance = "))

    print("\n***************\n")

    account = BankAccount(accountNumber, name, balance)

    sum = int(input("Sum = "))
    sub = int(input("Sub = "))

    print("\n***************\n")

    account.Deposit(sum)
    account.Withdrawal(sub)
    account.display()


if __name__ == '__main__':
    main()
