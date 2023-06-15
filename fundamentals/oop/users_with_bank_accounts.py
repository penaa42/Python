class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print('Balance: ' + ('%.2f' % self.balance))
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.05, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()


John = User("John", "john@email.com")
John.make_deposit(100).make_withdrawal(15).make_withdrawal(33).make_withdrawal(56).display_user_balance()