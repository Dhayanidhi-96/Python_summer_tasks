class BankAccount():
    def __init__(self,initial_balance = 0):
        self._balance = initial_balance
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self,amount):
        self._balance = amount

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited {amount}.New Balance : {self.balance}")
        else :
            print("❌ Deposited Amount Must be positive")

    def withdraw(self,amount):
        if amount <= 0:
            print("❌ Withdrawl amount must be positive")
        elif amount > self.balance:
            print("❌ insufficiant funds")
        else :
            self.balance -= amount
            print(f"withdrew {amount} .New Balance {self.balance}")
if __name__ == "__main__":
    account = BankAccount(10000)
    print("Current Balance :",account._balance)

    account.deposit(500)
    account.withdraw(5000)
    account.withdraw(20000)

    print("Final Balance :",account.balance)