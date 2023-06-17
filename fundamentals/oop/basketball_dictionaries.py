players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "Small Forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "Small Forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "oel Embiid",
        "age": 32,
        "position": "Power Forward",
        "team": "Philidelphia 76ers"
    },
    {
        "name": "",
        "age": 16,
        "position": "P",
        "team": "en"
    }
]

# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]
        print(self.name)

    def player_info(self):
        print(self)

    new_team = []

    def get_players(players):
        # print(players)
        for player in players:
            # print(player)
            # data = player
            pass


Player.get_players(players)

kevin = {
    "name": "Kevin Durant",
    "age": 34,
    "position": "Small Forward",
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum",
    "age": 24,
    "position": "Small Forward",
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving",
    "age": 32,
    "position": "Point Guard",
    "team": "Brooklyn Nets"
}

# player_kevin = Player(kevin)
# player_jason = Player(jason)
# player_kyrie = Player(kyrie)
# print(Player(kevin))