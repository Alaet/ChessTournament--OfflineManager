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
