# https://docs.python.org/fr/3/library/unittest.html
import random
import unittest

from .model import Player
from .controller import PlayerController
from .view import PlayerView

from Database.db_test import players_table_test


class TestPlayerModel(unittest.TestCase):

    @staticmethod
    def create_player():
        print("Creation d'une liste de 8 joueurs aléatoirement")
        players_list = []
        for x in range(0, 8):
            player = Player(name="Joueur"+str(x), lastname="LastName"+str(x), birthdate="22/12/92", gender="M",
                            rank=random.randrange(1, 50),
                            player_id=len(players_table_test.all()) + x)
            players_list.append(player)
            assert player
        assert 8, len(players_list)
        return players_list

    def test_adding_score(self):
        print("Adding Score")
        player = self.create_player()
        old_score = player[0].score
        player[0].add_score(0.5)
        new_score = player[0].score
        self.assertNotEqual(old_score, new_score)

    def test_update_score(self):
        players = self.create_player()
        for player in players:
            print("player : " + player.name + " rank : " + str(player.rank) + "\n")
        p_c = PlayerController(PlayerView, 0)
        p_c.update_rank(tournament_players=players)
        for player in players:
            print("player : " + player.name + " rank : " + str(player.rank) + "\n")
