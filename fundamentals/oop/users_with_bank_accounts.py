class BankAccount:
    def __init__(self, int_rate, bank_balance, saving_balance):
        self.int_rate = int_rate
        self.bank_balance = bank_balance
        self.saving_balance = saving_balance

    def bank_deposit(self, amount):
        if amount > 0:
            self.bank_balance += amount
        return self

    def save_deposit(self, amount):
        if amount > 0:
            self.saving_balance += amount
        return self

    def bank_withdrawal(self, amount):
        if self.bank_balance - amount < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.bank_balance -= 5
        else:
            self.bank_balance -= amount
        return self
    
    def save_withdrawal(self, amount):
        if self.saving_balance - amount < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.saving_balance -= 5
        else:
            self.saving_balance -= amount
        return self

    def display_bank_acc(self):
        print('bank balance: ' + ('%.2f' % self.bank_balance))
        # return self
    
    def display_save_acc(self):
        print('Saving balance: ' + ('%.2f' % self.saving_balance))

# class SavingAccount:
#     def __init__(self, int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         return self
    
#     def withdrawal(self, amount):
#         if self.balance - amount < 0:
#             print('Insufficient funds: Charging a $5 fee')
#             self.balance -= 5
#         else:
#             self.balance -= amount
#         return self
    
#     def display_account_info(self):
#         print('Balance: ' + ('%.2f' % self.balance))
#         return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.05, bank_balance = 0, saving_balance = 0)

    def make_bank_deposit(self, amount):
        self.account.bank_deposit(amount)
        return self
    
    def make_save_deposit(self, amount):
        self.account.save_deposit(amount)
        return self

    def make_bank_withdrawal(self, amount):
        self.account.bank_withdrawal(amount)
        return self

    def make_save_withdrawal(self, amount):
        self.account.save_withdrawal(amount)
        return self

    def user_bank_balance(self):
        self.account.display_bank_acc()

    def user_save_balance(self):
        self.account.display_save_acc()

John = User("John", "john@email.com")
Ben = User("Ben", "ben@email.com")

John.make_bank_deposit(100).make_bank_withdrawal(15).make_bank_withdrawal(33).make_bank_withdrawal(56).user_bank_balance()
Ben.make_save_deposit(100).make_save_withdrawal(15).make_save_withdrawal(33).make_save_withdrawal(56).user_save_balance()
# print(John.name)
# add functionality for multiple accounts per user
# look into reformating