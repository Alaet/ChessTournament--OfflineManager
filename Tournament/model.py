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

    def __repr__(self):
        new_name = self.name + "   / Date de début : " + self.date
        if self.description != "":
            new_name = new_name + "   / Description : " + self.description
        return new_name
