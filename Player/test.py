# https://docs.python.org/fr/3/library/unittest.html
import random
import unittest

from .model import Player


class TestPlayerModel(unittest.TestCase):

    def create_player(self):
        print("Creation d'une liste de 8 joueurs aléatoirement")
        players_list = []
        for x in range(0, 8):
            player = Player(name="Joueur"+str(x), lastname="LastName"+str(x), birthdate="22/12/92", gender="M",
                            rank=random.randrange(1, 50),
                            id=x)
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