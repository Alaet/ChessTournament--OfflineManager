# https://docs.python.org/fr/3/library/unittest.html
import unittest

from Player.test import TestPlayerModel
from .controller import TournamentController
from .view import TournamentView


class TestTournamentController(unittest.TestCase):

    def test_tournament_creation(self):
        print("Creation d'un tournoi à partir d'une liste de 8 joueurs aléatoire")
        players = TestPlayerModel.create_player(self=TestPlayerModel)
        tournament = TournamentController.create_tournament(TournamentController(TournamentView), all_players=players)
        assert tournament
        return tournament
