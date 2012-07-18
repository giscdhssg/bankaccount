# Filename: classes.py

class Account:
    ''' superclass for bank account '''

    def __init__(self, nAccountNo, nCustomerName, nBalance):
        ''' constructor for bank account '''
        self.__AccountNo = nAccountNo
        self.__CustomerName = nCustomerName
        self.__Balance = nBalance
    
    def getAccountNo(self):
        ''' accessor method for account number '''
        return self.__AccountNo
    
    def getCustomerName(self):
        ''' accessor method for customer name '''
        return self.__CustomerName
    
    def getBalance(self):
        ''' accessor method for balance '''
        return self.__Balance    

    def setBalance(self, newBalance):
        ''' modifier/mutator method for balance '''
        self.__Balance = newBalance

    def deposit(self, amount):
        ''' modifier/mutator to deposit to account '''
        self.__Balance = self.__Balance + amount

    def withdraw(self, amount):
        ''' modifier/mutator to withdraw from account '''
        self.__Balance = self.__Balance - amount

    def display(self):
        ''' helper/support method to display account info '''
        print("Account No:", self.__AccountNo)
        print("Customer Name:", self.__CustomerName)
        print("Balance:", self.__Balance)


class SavingAccount(Account): # inheritance
    ''' subclass for saving account '''
    
    def __init__(self, nAccountNo, nCustomerName, nBalance):
        ''' constructor for saving account '''
        super().__init__(nAccountNo, nCustomerName, nBalance)
        self.__interest = 0.01 / 12

    def display_monthly_statement(self):
        self.setBalance(self.getBalance() * (1 + self.__interest))
        print("Saving Account Monthly Statement")
        super().display()


class CurrentAccount(Account):
    ''' subclass for current account '''

    def __init__(self, nAccountNo, nCustomerName, nBalance):
        ''' constructor for saving account '''
        super().__init__(nAccountNo, nCustomerName, nBalance)

    def display_monthly_statement(self):
        print("Current Account Monthly Statement")
        super().display()





