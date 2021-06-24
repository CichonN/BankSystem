# --------------------------------------------------------------------------------------
# Assignment Name:      Banking System
# Name:                 Neina Cichon
# Date:                 2020-08-07
# --------------------------------------------------------------------------------------
#Create global variables
boolCheck = bool(False)
allBalance1 = float(0)
allBalance2 = float(0)
allBalance3 = float(0)
allBalance4 = float(0)


class Customer:

    def __init__(self, firstName, lastName, ssn):
        self.firstName = firstName
        self.lastName = lastName
        self.ssn = ssn

    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def ssn(self):
        return self.__ssn

    #Validate name
    @firstname.setter
    def firstname(self, firstname):
        if not firstname.isalpha():
             raise Exception('firstname cannot be a number.')
        else:
            self.__firstname = firstname

    #Validate name
    @lastname.setter
    def lastname(self, lastname):
        if not lastname.isalpha():
            raise Exception('lastname cannot be a number.')
        else:
            self.__lastname = lastname
    
    #Validate SSN
    @ssn.setter
    def ssn(self, ssn):
        if len(ssn) == 9:
            self.__ssn = ssn
            parts = ssn.split('-')
            return ssn
        else:
            raise Exception('SSN must be 9 digits.')

class Account(Customer):

    def __init__(self, firstName, lastName, ssn, accountNumber, accountType, balance, amount = 0):
        Customer.__init__(self,  firstName, lastName, ssn)
        self.accountNumber = accountNumber
        self.balance = balance  #Minimum of $0, else $20 per transaction
        self.amount = amount
        self.accountType = accountType
        
        #Track All Account Balance
        if ssn == customer1.ssn:
            global allBalance1
            allBalance1 += self.balance
            #return allBalance1
        elif ssn == customer2.ssn:
            global allBalance2
            allBalance2 += self.balance
            #return allBalance2
        elif ssn == customer3.ssn:
            global allBalance3
            allBalance3 += self.balance
            #return allBalance3
        elif ssn == customer4.ssn:
            global allBalance4
            allBalance4 += self.balance
            #return allBalance4

#--------------------------------------------------------------------------
#1. Function Name:   deposit      
#2. Function Description  deposits money into account
#--------------------------------------------------------------------------


    # Deposits (>= $0)
    def deposit(self, accountNumber, accountType, amount):
        self.accountType = accountType

        #Deposits for Checking Account
        if self.accountType.lower() == "checking":
            try:
                amount = float(amount)
            except ValueError:
                print("That isn't a number.", "\n--------------------------")
                return None
            if amount< 0:
                print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
                return None
     
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
        
        #Deposit for Savings Account
        elif self.accountType.lower() == "savings":
            try:
                amount = float(amount)
            except ValueError:
                print("That isn't a number.", "\n--------------------------")
                return None
            if amount< 0:
                print("Invalid input. Amount must be greater than 0.", "\n--------------------------")
                return None
            if amount >= 500:
                self.balance += amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyBalance = "${:,.2f}".format(self.balance)

                print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Deposited: ", currencyAmount, "\n--------------------------")
                return self.balance
            else:
                print("Deposit must be at least $500.00.", "\n--------------------------")
                return None

#--------------------------------------------------------------------------
#1. Function Name:   withdrawal      
#2. Function Description  withdrawals money from account
#--------------------------------------------------------------------------
    # Withrawals (>= $0)
    def withdrawal(self, accountNumber, accountType, amount):
        
        #Withdrawal for Checking Account
        if self.accountType.lower() == "checking":
            global boolCheck
            try:
                amount = float(amount)
            except ValueError:
                print("That isn't a number. Please enter a number.", "\n--------------------------")

                boolCheck = False
                return -1
            if amount< 0:
                print("Invalid input. Amount must be greater than 0.", "\n--------------------------")

                boolCheck = False
                return -1

            if (self.balance - amount) < 0:
                fee = 20
                self.balance -= fee
                self.balance -= amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyFee = "${:,.2f}".format(fee)
                currencyBalance = "${:,.2f}".format(self.balance)

                #print()        
                print("Account Number: ", self.accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\nOverdraft fee: ", currencyFee, "\n--------------------------")

                boolCheck = True
                return self.balance, boolCheck
            else:
                self.balance -= amount

                currencyAmount = "${:,.2f}".format(amount)
                currencyBalance = "${:,.2f}".format(self.balance)

                print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\n--------------------------")

                boolCheck = True
                return self.balance, boolCheck
        
        #Withdrawal for Savings Account
        elif self.accountType.lower() == "savings":
            if self.balance - amount < 500:
                print("Insufficient funds.", "\n--------------------------")

                boolCheck = False
                return None
            if amount< 0:
                print("Invalid input. Amount must be greater than 0.", "\n--------------------------")

                boolCheck = False
                return -1
            else:
                self.balance -= amount 

                currencyAmount = "${:,.2f}".format(amount)
                currencyBalance = "${:,.2f}".format(self.balance)

                print("Account Number: ", accountNumber, "\nAccount Holder:" , self.firstName , self.lastName, "\nAmount Withrawn: ", currencyAmount, "\n--------------------------")

                boolCheck = True
                return self.balance, boolCheck

#--------------------------------------------------------------------------
#1. Function Name:   transfer      
#2. Function Description  transfers money from one account to another
#--------------------------------------------------------------------------
    # Transferring Funds (>= $0)
    def transferFunds(self, accountType, receivingAccountNumber, receivingAccountType, amount): 
        #self.receivingAccountNumber = receivingAccountNumber
        global boolCheck
        boolCheck = False

        if amount > self.balance:
            print("Insufficient funds.", "\n--------------------------")

        else:
            try:
                self.withdrawal(self.accountNumber, accountType, amount)
                if boolCheck == True:  #Only proceed if withdrawal was successful
                    self.deposit(receivingAccountNumber, receivingAccountType, amount)
            except ValueError:
                print("If depositing into a savings account, amount must be at least $500.")



#--------------------------------------------------------------------------
### Create Customers
#--------------------------------------------------------------------------

customer1 = Customer("Dora", "Explorer",  "555889999")
customer2 = Customer("Sofia", "TheFirst", "444774444")
customer3 = Customer("Mickey", "Mouse", "588773333")
customer4 = Customer("Doc", "McStuffins", "222443333")


#--------------------------------------------------------------------------
### Create Accounts
#--------------------------------------------------------------------------

account1 = Account("Dora", "Explorer",  "555889999", "777777", "checking", 500.00)
account2 = Account("Sofia", "TheFirst","444774444", "888888", "checking", 0)
account3 = Account("Mickey", "Mouse", "588773333", "558855", "checking", -20)
account4 = Account("Sofia", "TheFirst","444774444", "995888", "checking", 2000)

account5 = Account("Mickey", "Mouse", "588773333", "444444", "savings", 500.77)
account6 = Account("Doc", "McStuffins", "222443333", "555555", "savings", 700.59)
account7 = Account("Dora", "Explorer", "555889999", "626262", "savings", 999.22)
account8 = Account("Dora", "Explorer", "555889999", "498882", "savings", 600.00)

#--------------------------------------------------------------------------
### Create Transactions
#--------------------------------------------------------------------------

transaction1 = account1.deposit("777777", "checking", -20) #Invalid
transaction2 = account2.withdrawal("888888", "checking", 20) #Success, plus fee
transaction3 = account3.deposit("558855", "checking", 20) #Success
transaction4 = account4.withdrawal("995888", "checking", 20) #Success
transaction5 = account5.deposit("444444", "savings", 20) #Invalid
transaction6 = account6.withdrawal("555555", "savings", -20) #Invalid
transaction7 = account7.deposit("626262", "savings", 2000) #Success
transaction8 = account8.withdrawal("498882", "savings", 700) #Insufficient Funds

#--------------------------------------------------------------------------
### Create Transfer Transactions
#--------------------------------------------------------------------------

account4.transferFunds("checking", "888888", "checking", 20) #Success
account3.transferFunds("checking", "555555", "savings", 2000) #Insufficient Funds
account1.transferFunds("checking", "995888", "checking", 200) #Success
account5.transferFunds("savings", "558855", "checking", 40) #Insufficient Funds
account6.transferFunds("savings","498882", "savings", 600) #Insufficient Funds
account8.transferFunds("savings", "777777", "checking", 100) #Success

#--------------------------------------------------------------------------
###Show All Account Balance for each Customer
#--------------------------------------------------------------------------

print(customer1.firstName, customer1.lastName, "- All Accounts Balance: ", "${:,.2f}".format(allBalance1))
print(customer2.firstName, customer2.lastName, "- All Account Balance: ", "${:,.2f}".format(allBalance2))
print(customer3.firstName, customer3.lastName, "- All Account Balance: ", "${:,.2f}".format(allBalance3))
print(customer4.firstName, customer4.lastName, "- All Account Balance: ", "${:,.2f}".format(allBalance4))