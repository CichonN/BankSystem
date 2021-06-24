

#class CheckingAccount(Customer):

#    def __init__(self, firstName, lastName, ssn, accountNumber, balance, amount = 0):
#        Customer.__init__(self,  firstName, lastName, ssn)
#        self.accountNumber = accountNumber
#        self.balance = balance  #Minimum of $0, else $20 per transaction
#        self.amount = amount

#    def balance(self): 
#        return self.balance

#    # Deposits (>= $0)
#    def deposit(self, accountNumber, amount):

#        try:
#            amount = float(amount)
#        except ValueError:
#            print("That isn't a number.", "\n--------------------------")
#            return -1
#        if amount< 0:
#            print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
#            return -1
     
#        if (self.balance + amount) < 0:
#            fee = 20
#            self.balance -= fee
#            self.balance += amount

#            currencyAmount = "${:,.2f}".format(amount)
#            currencyFee = "${:,.2f}".format(fee)
#            currencyBalance = "${:,.2f}".format(self.balance)
     
#            print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "Amount Withrawn: ", currencyAmount, "\nOverdraft fee: ", currencyFee, "\n--------------------------")
#            return self.balance

#        else:
#            self.balance += amount

#            currencyAmount = "${:,.2f}".format(amount)
#            currencyBalance = "${:,.2f}".format(self.balance)

#            print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Deposited: ", currencyAmount, "\n--------------------------")
#            return self.balance

#    # Withrawals (>= $0)
#    def withdrawal(self, accountNumber, amount):

#        try:
#            amount = float(amount)
#        except ValueError:
#            print("That isn't a number. Please enter a number.", "\n--------------------------")
#            return -1
#        if amount< 0:
#            print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
#            return -1

#        if (self.balance - amount) < 0:
#            fee = 20
#            self.balance -= fee
#            self.balance -= amount

#            currencyAmount = "${:,.2f}".format(amount)
#            currencyFee = "${:,.2f}".format(fee)
#            currencyBalance = "${:,.2f}".format(self.balance)

#            #print()        
#            print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\nOverdraft fee: ", currencyFee, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
#            return self.balance
#        else:
#            self.balance -= amount

#            currencyAmount = "${:,.2f}".format(amount)
#            currencyBalance = "${:,.2f}".format(self.balance)

#            print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
#            return self.balance

#    def currentBalance(self):
#        currencyBalance = "${:,.2f}".format(self.balance)
#        print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
#        return currencyBalance

#    # Transferring Funds (>= $0)
#    def transferFunds(self, receivingAccountNumber, accountType, amount): 
#        #self.receivingAccountNumber = receivingAccountNumber

#        if accountType == "checking":
#            if self.balance - amount < 0:
#                print("Insufficient funds.", "\n--------------------------")

#            else:
#                self.withdrawal(self.accountNumber, amount)
#                self.deposit(receivingAccountNumber, amount)
#        else:
#            self.withdrawal(self.accountNumber, amount)
#            SavingsAccount.deposit(receivingAccountNumber, amount)

#class SavingsAccount(Customer):
    
#    def __init__(self, firstName, lastName, ssn, accountNumber, balance, amount = 0):
#        Customer.__init__(self,  firstName, lastName, ssn)
#        self.accountNumber = accountNumber
#        self.balance = balance  #Minimum of $500
#        self.amount = amount

#    # Deposits (>= $500)
#    def deposit(self, accountNumber, amount):
#        try:
#            amount = float(amount)
#        except ValueError:
#            print("That isn't a number.", "\n--------------------------")
#            return -1
#        if amount< 0:
#            print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
#            return -1
#        if amount >= 500:
#            self.balance += amount

#            currencyAmount = "${:,.2f}".format(amount)
#            currencyBalance = "${:,.2f}".format(self.balance)

#            print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Deposited: ", currencyAmount, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
#            return self.balance
#        else:
#            print("Deposit must be at least $500.00.", "\n--------------------------")
#            return None

#    # Withrawals (>= $0)
#    def withdrawal(self, accountNumber, amount):
#        if self.balance - amount < 500:
#            print("Insufficient funds.", "\n--------------------------")
#            return None
#        else:
#            self.balance -= amount 

#            currencyAmount = "${:,.2f}".format(amount)
#            currencyBalance = "${:,.2f}".format(self.balance)

#            print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
#            return self.balance

#        # Transferring Funds (>= $0)
#    def transferFunds(self, receivingAccountNumber, accountType, amount): 
#        #self.receivingAccountNumber = receivingAccountNumber

#        if accountType == "savings":
#            if self.balance - amount < 0:
#                print("Insufficient funds.", "\n--------------------------")

#            else:
#                self.withdrawal(self.accountNumber, amount)
#                self.deposit(receivingAccountNumber, amount)
#        else:
#            self.withdrawal(self.accountNumber, amount)
#            CheckingAccount.deposit(receivingAccountNumber, amount)



class Account(Customer):

    def __init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0):
        Customer.__init__(self,  firstName, lastName, ssn)
        self.accountNumber = accountNumber
        self.accountType = accountType
        self.balance = balance  #Minimum of $0, else $20 per transaction
        self.amount = amount
        
        try:
            accountType = str(accountType)
        except ValueError:
                    print("Invalid input.")
        #if accountType.lower() == "checking":
        #    checking()
        #elif accountType.lower() == "savings":
        #    savings()
        

    #def balance(self): 
    #    return self.balance
    
class Checking(Account):
    def __init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0):
        Account.__init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0)
        Savings.__init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0)

        #if self.accountType == "checking":
            # Deposits (>= $0)
        def deposit(self, accountNumber, amount):

            try:
                amount = float(amount)
            except ValueError:
                print("That isn't a number.", "\n--------------------------")
                return -1
            if amount< 0:
                print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
                return -1
     
            if (self.balance + amount) < 0:
                fee = 20
                self.balance -= fee
                self.balance += amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyFee = "${:,.2f}".format(fee)
                currencyBalance = "${:,.2f}".format(self.balance)
     
                print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "Amount Withrawn: ", currencyAmount, "\nOverdraft fee: ", currencyFee, "\n--------------------------")
                return self.balance

            else:
                self.balance += amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyBalance = "${:,.2f}".format(self.balance)

                print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Deposited: ", currencyAmount, "\n--------------------------")
                return self.balance

        # Withrawals (>= $0)
        def withdrawal(self, accountNumber, amount):

            try:
                amount = float(amount)
            except ValueError:
                print("That isn't a number. Please enter a number.", "\n--------------------------")
                return -1
            if amount< 0:
                print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
                return -1

            if (self.balance - amount) < 0:
                fee = 20
                self.balance -= fee
                self.balance -= amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyFee = "${:,.2f}".format(fee)
                currencyBalance = "${:,.2f}".format(self.balance)

                #print()        
                print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\nOverdraft fee: ", currencyFee, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
                return self.balance
            else:
                self.balance -= amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyBalance = "${:,.2f}".format(self.balance)

                print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
                return self.balance

        def currentBalance(self):
            currencyBalance = "${:,.2f}".format(self.balance)
            print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
            return currencyBalance

        # Transferring Funds (>= $0)
        def transferFunds(self, receivingAccountNumber, accountType, amount): 
            #self.receivingAccountNumber = receivingAccountNumber

            if accountType == "checking":
                if self.balance - amount < 0:
                    print("Insufficient funds.", "\n--------------------------")

                else:
                    self.withdrawal(self.accountNumber, amount)
                    self.deposit(receivingAccountNumber, amount)
            else:
                self.withdrawal(self.accountNumber, amount)
                Savings.deposit(receivingAccountNumber, amount)
class Savings(Account, Checking):
    def __init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0):
        Account.__init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0)
        Checking.__init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0)

    #elif self.accountType == "savings":

        # Deposits (>= $500)
        def deposit(self, accountNumber, amount):
            try:
                amount = float(amount)
            except ValueError:
                print("That isn't a number.", "\n--------------------------")
                return -1
            if amount< 0:
                print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
                return -1
            if amount >= 500:
                self.balance += amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyBalance = "${:,.2f}".format(self.balance)

                print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Deposited: ", currencyAmount, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
                return self.balance
            else:
                print("Deposit must be at least $500.00.", "\n--------------------------")
                return None

        # Withrawals (>= $0)
        def withdrawal(self, accountNumber, amount):
            if self.balance - amount < 500:
                print("Insufficient funds.", "\n--------------------------")
                return None
            else:
                self.balance -= amount 

                currencyAmount = "${:,.2f}".format(amount)
                currencyBalance = "${:,.2f}".format(self.balance)

                print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\nCurrentBalance:", currencyBalance, "\n--------------------------")
                return self.balance

            # Transferring Funds (>= $0)
        def transferFunds(self, receivingAccountNumber, accountType, amount): 
            #self.receivingAccountNumber = receivingAccountNumber

            if accountType == "savings":
                if self.balance - amount < 0:
                    print("Insufficient funds.", "\n--------------------------")

                else:
                    self.withdrawal(self.accountNumber, amount)
                    self.deposit(receivingAccountNumber, amount)
            else:
                self.withdrawal(self.accountNumber, amount)
                Checking.deposit(receivingAccountNumber, amount)

