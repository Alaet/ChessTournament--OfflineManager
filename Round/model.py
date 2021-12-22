from Match.model import Match


class Round(object):

    def __init__(self, tournament):

        self.tournament = tournament
        self.round_name = str
        self.round_starting_date = None
        self.round_ending_date = None
        self.match_history = []

    def sort_players_as_dict(self, players):
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
                           "player_data": {"id": player.id, "score": player.score, "rank": player.rank, "history": []}
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

    def generate_pair_from_id(self, list_rank_players_sorted):
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

        round_pair_player_list = []

        for match in versus:
            opponents = [(sorted_list[match[0]], sorted_list[match[0]].score),
                         (sorted_list[match[1]], sorted_list[match[1]].score)]

            round_pair_player_list.append(Match(opponents))
        self.match_history = round_pair_player_list
        return round_pair_player_list
