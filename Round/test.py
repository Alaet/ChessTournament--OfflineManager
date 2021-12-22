import unittest

from Tournament.test import TestTournamentController
from .controller import RoundController
from Tournament.controller import TournamentController


class TestRoundController(unittest.TestCase):

    def test_generate_round(self):
        tournament = TestTournamentController.test_tournament_creation(TestTournamentController)
        test_round = RoundController.generate_round(RoundController, tournament=tournament)
        return test_round.match_history[0], tournament

    def test_cloture_round(self):
        round = self.test_generate_round()
        TournamentController.cloture_round(TournamentController, round)
        self.assertTrue(len(round.round_ending_date) > 0)

    def test_evaluate_match(self):
        match_tournament = self.test_generate_round()
        TournamentController.evaluate_match(TournamentController, match_tournament[0],
                                            match_tournament[1])
