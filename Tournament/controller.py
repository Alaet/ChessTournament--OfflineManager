from .model import Tournament
from .serialize import serialize_tournament_players


class TournamentController:
    def __init__(self, view):
        self.view = view

    def create_tournament(self, all_players):
        """
        Prompt for tournament details, and players from list(all_players) of object(Player) to pick
        to return an object(Tournament)
        :param all_players: list(object(Player))
        :return: object(Tournament)
        """
        name = self.view.prompt_for_tournament_name()
        place = self.view.prompt_for_tournament_place()
        date = self.view.prompt_for_tournament_date()
        time_mode = self.view.prompt_for_time_mode()
        players = self.view.pick_players_for_tournament(all_players)
        serialized_players = serialize_tournament_players(players)
        description = self.view.prompt_for_description()
        new_tournament = Tournament(name, place, date, time_mode, serialized_players, description)

        return new_tournament

    @staticmethod
    def display_tournament_result(matches):
        """
        Display sorted players based on player score
        :param matches:
        :return:
        """
        tournament_result = []
        for match in matches:
            tournament_result.append((match['match_info'][0][0]['name'], str(match['match_info'][0][0]['score'])))
            tournament_result.append((match['match_info'][1][0]['name'], str(match['match_info'][1][0]['score'])))
            tournament_result.sort(reverse=True, key=lambda x: x[1])

        for x in range(len(tournament_result)):
            print(tournament_result[x][0] + "  -  Score  :  " + tournament_result[x][1])

        print("\n\nLe gagnant est " + tournament_result[0][0] + " ! ! !\n\n")
