class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}')
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print('already a rewards member')
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        if self.gold_card_points - amount <= 0:
            print('not enough points remaining')
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self

person1 = User('John', 'Doe', 'JohnDoe@email.com', 30)

person2 = User('Jane', 'Smith', 'JaneSmith@email.com', 22)

person3 = User('Dude', 'Guy', 'DudeGuy@email.com', 40)

person1.display_info().enroll().display_info().enroll()
person2.display_info().enroll().spend_points(50).display_info()
person3.display_info().enroll().spend_points(80).spend_points(100).spend_points(40)


