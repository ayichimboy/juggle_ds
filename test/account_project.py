from scripts import *

dave = bank_account('dave',1000)
sarah = bank_account('sarah',1000)

# setup the charactors
dave.getBalance()
sarah.getBalance()

# Amount
sarah.deposit(500)

# withdraw amount from dave
dave.withdraw(100000)
dave.withdraw(50)

#transfer ammount
dave.transfer(sarah,100)