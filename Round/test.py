# https://docs.python.org/fr/3/library/unittest.html
import unittest

from .controller import RoundController
from .model import Round
from .view import RoundView

from Tournament.model import Tournament

from Player.test import TestPlayerModel

from Match.controller import MatchController


class TestRoundController(unittest.TestCase):

    def test_generate_round(self, tournament):
        test_round = RoundController.generate_round(RoundController(RoundView), tournament=tournament)
        return test_round.match_history[0]

    def test_cloture_round(self):
        tournament = Tournament("lol", "ici", "22.12.92", "Bul", TestPlayerModel.create_player(), [])
        new_round = Round(tournament)
        RoundController.cloture_round(new_round)
        self.assertTrue(len(new_round.round_ending_date) > 0)

    def test_evaluate_match(self):
        tournament = Tournament("lol", "ici", "22.12.92", "Bul", TestPlayerModel.create_player(), [])
        new_round = RoundController.generate_round(RoundController(RoundView), tournament=tournament)
        match_tournament = new_round.match_history
        for match in match_tournament:
            MatchController.evaluate_match(match, tournament)
