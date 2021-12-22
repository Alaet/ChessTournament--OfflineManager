import datetime

from Round.model import Round


class RoundController(object):

    def __init__(self, view):
        self.view = view

    def generate_round(self, tournament):
        """
        Generate a round based on player in tournament given in parameters
        :param tournament: object(Tournament)
        :return: object(Round) as new_round
        """
        new_round = Round(tournament)
        sorted_list = new_round.sort_players_as_dict(tournament.players_list)
        versus = new_round.generate_pair_from_id(sorted_list)
        new_round.generate_match_list(tournament.players_list, versus)
        new_round.round_name = "Round " + str(tournament.round_count)
        tournament.round_count += 1

        new_round.round_starting_date = datetime.datetime.now()
        new_round.round_starting_date = new_round.round_starting_date.strftime("%Y-%m-%d %H:%M:%S")
        return new_round
