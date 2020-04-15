#Object Orientated Programming Challenge Video 68

class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance= balance
        
    def withdraw(self, amount):
        if self.balance < abs(amount):
            print("Funds are not available")
        else:
            self.balance = self.balance - amount
    
    def deposit(self,damount):
        self.balance = self.balance + damount
        
    def __str__(self):
        return "Owner : {} \nBalance : R{}".format(self.owner,self.balance)
    

#Testing Account Class
acct1=Account("Raymond",900.10)

print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.withdraw(0.10)
print(acct1.balance)

acct1.deposit(1000)
print(acct1.balance)

acct1.withdraw(-5000)
print(acct1.balance)