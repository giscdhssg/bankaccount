# monthly_statement.py

from classes import *

# main
if __name__ == "__main__":
    try:
        # open files for input
        account_file = open("ACCOUNTS.DAT", 'r')
        transaction_file = open("TRANSACTIONS.DAT", 'r') 

        # read all lines from account file
        account_lines = account_file.readlines()

        # read all lines from transaction file
        transaction_lines = transaction_file.readlines()
        
        # loop through all accounts
        for account_line in account_lines:
            # get account details
            account_no = account_line[:6]
            customer_name = account_line[6:35]
            balance = float(account_line[35:])
            if account_no[0] == 'S':
                # create saving account object
                account = SavingAccount(account_no, customer_name, balance)
            else:
                # create current account object
                account = CurrentAccount(account_no, customer_name, balance)
            #account.display()

            # loop through all transactions
            for transaction_line in transaction_lines:
                # get transaction details
                transaction_date = transaction_line[:8]
                transaction_account = transaction_line[8:14]
                transaction_type = transaction_line[14:15]
                transaction_amount = float(transaction_line[15:])
                # if relevant account
                if transaction_account == account_no:
                    if transaction_type == 'D': # deposit
                        account.deposit(transaction_amount)
                    else: # withdraw
                        account.withdraw(transaction_amount)

            # output monthly statement
            account.display_monthly_statement()
            print()

        # close files
        account_file.close()
        transaction_file.close()

    except IOError:
        # cannot open account or transaction file for input
        print("Error reading ACCOUNTS.DAT or TRANSACTIONS.DAT.")
