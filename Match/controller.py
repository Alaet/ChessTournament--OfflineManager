from .model import Match
from Tournament.controller import TournamentController

class MatchController:

    def generate_match_list(self, sorted_list, versus):
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
        serealized_players = TournamentController.serialize_tournament_players(TournamentController, sorted_list)
        round_pair_player_list = []
        serialized_round_pair_player_list = []
        for match in versus:
            opponents = [(serealized_players[match[0]], sorted_list[match[0]].score),
                         (serealized_players[match[1]], sorted_list[match[1]].score)]
            current_match = Match(opponents)
            serialized_current_match = self.serialize_match(current_match)
            serialized_round_pair_player_list.append(serialized_current_match)
            round_pair_player_list.append(current_match)
        return serialized_round_pair_player_list

    @staticmethod
    def serialize_match(match):
        serialized_match = {
            'match_info': match.match_info
        }
        return serialized_match
