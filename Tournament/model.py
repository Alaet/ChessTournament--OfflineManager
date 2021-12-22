class Tournament:

    def __init__(self, name, place, date, player):
        self.match_count = 0
        self.round_count = 1
        self.name = name
        self.players_list = player
        self.rounds = []
        self.turn = 4
        self.place = place
        self.date = date
        self.close = False

