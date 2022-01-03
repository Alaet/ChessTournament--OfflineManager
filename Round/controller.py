import datetime
from Match.controller import MatchController
from .model import Round


class RoundController(object):
    def __init__(self, view):
        self.view = view

    def generate_round(self, tournament):
        """
        Generate a round based on player in tournament given in parameters
        :param tournament: object(Tournament)
        :return: object(Round) as new_round
        """

        sorted_list = self.sort_players_as_dict(tournament.players_list)
        versus = self.generate_pair_from_id(sorted_list)
        matches = MatchController.generate_match_list(sorted_list=tournament.players_list, versus=versus)
        new_round = Round(matches)

        new_round.round_name = "Round " + str(tournament.round_count)
        tournament.round_count += 1

        new_round.round_starting_date = datetime.datetime.now()
        new_round.round_starting_date = new_round.round_starting_date.strftime("%Y-%m-%d %H:%M:%S")
        return new_round

    @staticmethod
    def sort_players_as_dict(players):
        """
        Take list of Player as parameter and return a sorted dict by id/score(rank)
        with Player as Object and player_datas as dict
        :param players: list(object(Player))
        :return: dict{"player": object(Player),
                      "player_data" : dict{int, int, int, list}
                      }
        """
        players_sorted = []
        for x, player in enumerate(players):
            player_data = {"player": player,
                           "player_data": {"id": player['id'], "score": player['score'], "rank": player['rank'],
                                           "history": []}
                           }
            players_sorted.append(player_data)

            players_sorted.sort(key=lambda row: (row.get("id"), row.get("score"), row.get("rank")), reverse=True)

            for i in range(0, len(players_sorted)):
                for j in range(0, len(players_sorted) - i - 1):
                    if players_sorted[j]["player_data"]["score"] == players_sorted[j + 1]["player_data"]["score"]:
                        if players_sorted[j]["player_data"]["rank"] > players_sorted[j + 1]["player_data"]["rank"]:
                            temp = players_sorted[j]
                            players_sorted[j] = players_sorted[j + 1]
                            players_sorted[j + 1] = temp
        return players_sorted

    @staticmethod
    def generate_pair_from_id(list_rank_players_sorted):
        """
        Take sorted dict of object(Player) and player_datas
        to return tuple of versus based on object(Player) id
        :param list_rank_players_sorted: list(dict{"player": object(Player),
                                                   "player_data" : dict{int, int, int, list}
                                                   })
        :return: tuple[(versus_as_id),(versus_as_id),(versus_as_id),(versus_as_id)]
        """
        players = list_rank_players_sorted
        median = int(len(players) / 2)
        versus_as_id = []
        ID, HISTORY = 0, 3
        if len(players[0]["player_data"]["history"]) == 0:
            for i in range(median):
                versus_as_id.append((players[i]["player_data"]["id"], players[i + median]["player_data"]["id"]))
        else:
            i = 1
            while len(players) > 0:
                player_1, player_2 = players[ID], players[i]
                if player_2[ID] in player_1[HISTORY]:
                    i += 1
                else:
                    versus_as_id.append((player_1[ID], player_2[ID]))
                    del players[i]
                    del players[ID]
                    i = 1

        return versus_as_id
