import datetime
import pytz


class Accounts:
    """Simple account manage class"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print(f'Account for {self.name} has been created')

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.check_account()
            self.transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Accounts._current_time(), -amount))
        else:
            print(f'You do not have enough units on the account. Balance: {self.balance}')

    def check_account(self):
        print(f'Balance is: {self.balance}')

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = 'deposited'
            else:
                tran_type = 'withdraw'
                amount *= -1
            print(f'{amount}UNI, {tran_type} on {date}, {date.astimezone()}')


john = Accounts('John', 0)
john.deposit(1000)
john.withdraw(500)
john.show_transaction()


