from Match.model import Match


class Round(object):

    def __init__(self, tournament, matches):

        self.tournament = tournament
        self.round_name = str
        self.round_starting_date = None
        self.round_ending_date = None
        self.match_history = matches
