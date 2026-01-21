# build a functioning object oreinted program
class BlanceException(Exception):
    pass


# create the class
class bank_account:
    
    # use __init__ to initialize class creation 
    # __init__ is a decorator
    def __init__(self, accountname, amount):
        
        self.accountname = accountname
        self.amount      = amount           
        
        print(f"\nAccount '{self.accountname}' created.\nBalance = $'{self.amount:.2f}'")
    
    # add an method to the code
    def getBalance(self):
        print(f"\nAccount '{self.accountname}' balance = $ {self.amount:.2f}")
        
    # add another method
    def deposit(self, balance):
        self.amount = self.amount + balance
        print("\nDeposit complete...")
        self.getBalance()
        
    def viableTransaction(self, balance):
        if self.amount >= balance:
            return
        else:
            raise BlanceException(
                f"\nSorry, account '{self.accountname}' only has ${self.amount:.2f}"
            )
            
    def withdraw(self, balance):
        try:
            self.viableTransaction(balance)
            self.amount = self.amount - balance
            print("\nWithdraw Complete")
            self.getBalance()
        except BaseException as error:
            print(f'\nWithdraw interrupted: {error}')
            
            
    def transfer(self, acccountname, amount):
        try:
            print('\n*******\n\nBeginning Transfer.. 🚀🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            acccountname.deposit(amount)
            print('\nTransfer complete! ✅✅✅✅\n\n**********')
        except BaseException as error:
            print(f'\nTransfer interrupted: ❌❌ {error}')
            
# inhertitance
class InterestRewardsAcct(bank_account):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite Complete..😀😀")
        self.getBalance()
