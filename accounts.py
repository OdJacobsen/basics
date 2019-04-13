class Accounts:
    """Simple account manage class"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f'Account for {self.name} has been created')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.check_account()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print(f'You do not have enough units on the account. Balance: {self.balance}')

    def check_account(self):
        print(f'Balance is: {self.balance}')


john = Accounts('John', 0)
john.deposit(1000)
john.withdraw(3000)


