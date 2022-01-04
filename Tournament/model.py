class Tournament:

    def __init__(self, name, place, date, time_mode, player, description):
        self.match_count = 0
        self.round_count = 1
        self.name = name
        self.players_list = player
        self.rounds = []
        self.turn = 4
        self.place = place
        self.date = date
        self.close = False
        self.time_mode = time_mode
        self.description = description

    def __str__(self):
        return self.name + "   / Date de début : " + self.date
