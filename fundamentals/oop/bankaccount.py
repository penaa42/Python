class BankAccount:
    all_account_instances = []

    def __init__(self, balance = 0, int_rate = 0.01):
        self.int_rate = int_rate
        self.balance = balance

        collect_inst_info = {}
        collect_inst_info['balance'] = self.balance
        collect_inst_info['int_rate'] = self.int_rate
        BankAccount.all_account_instances.append(collect_inst_info)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('Error, cannot deposit the amount')
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print('Balance: ' + ('%.2f' % self.balance))

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate) 
        return self
    
    @classmethod
    def all_account_info(cls):
        print(cls.all_account_instances)


account_one = BankAccount(5, 0.05)
account_one.deposit(10).deposit(50).deposit(4).withdraw(33).yield_interest().display_account_info()

account_two = BankAccount()
account_two.deposit(100).deposit(15).withdraw(50).withdraw(23).withdraw(15).withdraw(60).yield_interest().display_account_info()

BankAccount.all_account_info()