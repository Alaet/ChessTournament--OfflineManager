class Round:

    def __init__(self, match_list):

        self.round_name = str
        self.round_starting_date = None
        self.round_ending_date = None
        self.match_history = match_list

    def __str__(self):
        return self.round_name
