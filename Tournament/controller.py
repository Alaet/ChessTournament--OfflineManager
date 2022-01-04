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
    def evaluate_match(match, tournament):
        """
        Prompt for winner from matched player then add score to this player
        and return match number index for this round
        :param match: tuple[(object(Player), player.score), (obect(Player), player.score)]
        :param tournament: object(Tournament)
        :return: int(tournament.match_count)
        """
        if tournament.match_count < 4:
            tournament.match_count += 1
        else:
            tournament.match_count = 1

        print("Match " + str(tournament.match_count) + "    ( 0 - Menu principal )\n1." + str(match['match_info'][0][0]
                                                                                              ['name']) + "\n\n2."
              + str(match['match_info'][1][0]['name']) + "\n3. Match nul")
        result = input()
        if result == "0":
            tournament.match_count -= 1
            return result
        elif result == "1":
            winner_p1 = next(item for item in tournament.players_list if item.id == match['match_info'][0][0]['id'])
            match['match_info'][0][0]['score'] += 1
            match['evaluated'] = True
            winner_p1.score = match['match_info'][0][0]['score']

        elif result == "2":
            winner_p2 = next(item for item in tournament.players_list if item.id == match['match_info'][1][0]['id'])
            match['match_info'][1][0]['score'] += 1
            match['evaluated'] = True
            winner_p2.score = match['match_info'][1][0]['score']

        elif result == "3":
            tie_p1 = next(item for item in tournament.players_list if item.id == match['match_info'][0][0]['id'])
            tie_p2 = next(item for item in tournament.players_list if item.id == match['match_info'][1][0]['id'])
            match['match_info'][0][0]['score'] += (1 / 2)
            match['match_info'][1][0]['score'] += (1 / 2)
            match['evaluated'] = True
            tie_p1.score = match['match_info'][0][0]['score']
            tie_p2.score = match['match_info'][1][0]['score']
        else:
            print("******* Choix invalide *******")
            tournament.match_count -= 1

        return tournament.match_count

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
