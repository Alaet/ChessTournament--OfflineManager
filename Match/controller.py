from .model import Match


class MatchController:

    @staticmethod
    def generate_match_list(sorted_list, versus):
        """
        Take sorted dict and versus as ID to create tuple of match with object(Player) and player.score
        :param sorted_list: dict{"player": object(Player),
                                 "player_data" : dict{int, int, int, list}
                                 }
        :param versus: tuple[(versus_as_id),(versus_as_id),(versus_as_id),(versus_as_id)]
        :return: tuple[
                        [(Player, player.score), (Player, player.score)],
                        [(Player, player.score), (Player, player.score)],
                        [(Player, player.score), (Player, player.score)],
                        [(Player, player.score), (Player, player.score)]
                      ]
        """
        round_pair_player_list = []
        for match in versus:

            first_player = next(item for item in sorted_list if item["id"] == match[0])

            second_player = next(item for item in sorted_list if item["id"] == match[1])
            try:
                opponents = [(first_player, first_player.score), (second_player, second_player.score)]
            except AttributeError:
                opponents = [(first_player, first_player['score']), (second_player, second_player['score'])]
            evaluated = False
            current_match = Match(opponents, evaluated)

            round_pair_player_list.append(current_match)
        return round_pair_player_list

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
