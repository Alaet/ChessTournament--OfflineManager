# https://docs.python.org/fr/3/library/unittest.html
import random
import unittest

from .model import Player

from Database.controller import players_table


class TestPlayerModel(unittest.TestCase):

    @staticmethod
    def create_player():
        print("Creation d'une liste de 8 joueurs aléatoirement")
        players_list = []
        for x in range(0, 8):
            player = Player(name="Joueur" + str(len(players_table.all()) + x), lastname="LastName" + str(len(
                players_table.all()) + x), birthdate=str(random.randrange(1, 30))
                                                     + "/" + str(random.randrange(1, 12)) + "/" + str(
                random.randrange(1950, 2000)), gender="M", rank=random.randrange(1, 50), player_id=len(
                players_table.all()) + x, score=0)
            players_list.append(player)
            assert player

        assert 8, len(players_list)
        return players_list
