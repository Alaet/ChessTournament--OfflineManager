import unittest
from .controller import RoundController
from Tournament.controller import TournamentController
from Tournament.model import Tournament
from Player.test import TestPlayerModel
from Round.model import Round


class TestRoundController(unittest.TestCase):

    def test_generate_round(self):
        tournament = Tournament("lol", "ici", "22.12.92", "Bul", TestPlayerModel.create_player(TestPlayerModel), [])
        test_round = RoundController.generate_round(RoundController, tournament=tournament)
        return test_round.match_history[0], tournament

    def test_cloture_round(self):
        tournament = Tournament("lol", "ici", "22.12.92", "Bul", TestPlayerModel.create_player(TestPlayerModel), [])
        round = Round(tournament)
        TournamentController.cloture_round(round)
        self.assertTrue(len(round.round_ending_date) > 0)

    def test_evaluate_match(self):
        tournament = Tournament("lol", "ici", "22.12.92", "Bul", TestPlayerModel.create_player(TestPlayerModel), [])
        round = RoundController.generate_round(RoundController, tournament=tournament)
        match_tournament = round.match_history
        for match in match_tournament:
            TournamentController.evaluate_match(match, tournament)
