# https://docs.python.org/fr/3/library/unittest.html
import unittest

from .controller import TournamentController
from .view import TournamentView


class TestTournamentController(unittest.TestCase):

    def test_tournament_creation(self, players_list):
        print("Creation d'un tournoi à partir d'une liste de 8 joueurs aléatoire")
        tournament = TournamentController.create_tournament(TournamentController(TournamentView),
                                                            all_players=players_list)
        assert tournament
        return tournament
