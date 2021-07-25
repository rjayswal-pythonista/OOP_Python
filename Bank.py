from random import randint
from abc import ABCMeta, abstractmethod


class Bank(metaclass=ABCMeta):

    @abstractmethod
    def createaccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withdraw(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displaybalance(self):
        return 0


class savingsAccount(Bank):

    def __init__(self):
        self.savingsaccount = {}

    def createaccount(self, name, depositamt):
        self.name = name
        self.depositamt = depositamt
        self.accountno = randint(10000, 99999)
        self.savingsaccount[self.accountno] = [name, depositamt]
        print()
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(f"SBI Account creation Successful for {self.name}. Your Account Number is {self.accountno}")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        self.displaybalance()

    def authenticate(self, name, accountnu):
        if accountnu in self.savingsaccount.keys():
            if self.savingsaccount[accountnu][0] == name:
                print()
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("User Authentication Successful")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                self.accountno = accountnu
                return True
            else:
                print()
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print(f"User Authentication Failed, invalid Customer Name {name}")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                return False
        else:
            print()
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("User Authentication Failed, invalid Account Number")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            return False

    def withdraw(self, withdrawamt):
        if withdrawamt > self.savingsaccount[self.accountno][1]:
            print()
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("Withdrawal amount exceeds account Balance. Withdrawal Unsuccessful")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        else:
            self.savingsaccount[self.accountno][1] -= withdrawamt
            print()
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(f"Withdrawal Successful. Rs. {withdrawamt} now withdrawn from your Account")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            self.displaybalance()

    def deposit(self, depositamt):
        self.savingsaccount[self.accountno][1] += depositamt
        self.displaybalance()

    def displaybalance(self):
        print()
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print(f"Account Balance for {self.name} is Rs. {self.savingsaccount[self.accountno][1]}")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

if __name__ == "__main__":

    savingsAccount = savingsAccount()
    print("###########################################################################################################")
    print("                                            Welcome to SBI Bank                                            ")
    print("###########################################################################################################")

    while True:
        print("Enter 1 if you wish to open an account with SBI")
        print("Enter 2 if you're an existing SBI Customer")
        print("Enter 3 to quit")
        userchoice = int(input())

        if userchoice == 1:
            print("Enter your Name")
            name = str(input())
            print("Enter the initial deposit amount")
            damt = int(input())
            savingsAccount.createaccount(name, damt)

        elif userchoice == 2:
            print("Please provide your Account Name")
            name = str(input())
            print("Please provide your 5 digit Account Number")
            accnu = int(input())
            validate = savingsAccount.authenticate(name, accnu)
            if validate is True:
                while True:
                    print("Enter 1 to withdraw money from your Account")
                    print("Enter 2 to deposit money into your Account")
                    print("Enter 3 to display your available balance")
                    print("Enter 4 to go back to previous menu")
                    choice = int(input())
                    if choice == 1:
                        print("Enter amount to withdraw")
                        withdrawamount = int(input())
                        savingsAccount.withdraw(withdrawamount)
                    elif choice == 2:
                        print("Enter amount to deposit")
                        depositamount = int(input())
                        savingsAccount.deposit(depositamount)
                    elif choice == 3:
                        savingsAccount.displaybalance()
                    elif choice == 4:
                        break

        elif userchoice == 3:
            print()
            print("###################################################################################################")
            print("Thank you for Banking with SBI. Have a wonderful Day!!!")
            print("###################################################################################################")
            quit()
