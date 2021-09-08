#Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.

class BankAccount():
    def __init__(self, accountNumber, name, balance):

        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

#Create a constructor with parameters: accountNumber, name, balance.

    def __init__(self, accountNumber, name, balance):

        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

#Create a Deposit() method which manages the deposit actions.

def Deposit(self, sum):

    self.balance = self.balance + sum

#Create a Withdrawal() method which manages withdrawals actions.

def Withdrawal(self, sub):

    if self.balance < sub:

        print("Out of money\n")
    else:

        self.balance = self.balance - sub

#Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.

def bankFees(self):

    self.balance = self.balance - (self.balance * 0.5)

#Create a display() method to display account details.

def display(self):

    print("Name : ", self.name)
    print("AccountNumber : ", self.accountNumber)
    print("Balance : ", self.balance)
    print("\n")

#Give the complete code for the BankAccount class.

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
