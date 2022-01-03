# https://docs.python.org/fr/3/library/unittest.html
import unittest

from Player.test import TestPlayerModel
from .controller import TournamentController
from .view import TournamentView
from Menu.view import View


class TestTournamentController(unittest.TestCase):

    def test_tournament_creation(self, players_list):
        print("Creation d'un tournoi à partir d'une liste de 8 joueurs aléatoire")
        tournament = TournamentController.create_tournament(TournamentController(TournamentView), all_players=players_list)
        assert tournament
        return tournament

    def display_players(self):
        players = TestPlayerModel.create_player()
        View.display_all_players(players)
