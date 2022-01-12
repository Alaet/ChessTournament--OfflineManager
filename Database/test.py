# https://docs.python.org/fr/3/library/unittest.html
import unittest

import tinydb

from .controller import players_table
from .controller import tournament_table
from .controller import deserialize_tournament

from Tournament.view import TournamentView
from Tournament.controller import TournamentController
from Tournament.serialize import deserialized_every_players, serialize_tournament, serialize_tournament_players

from Player.test import TestPlayerModel
from Player.serialize import serialize_player

from Round.controller import RoundController
from Round.serialize import serialize_round
from Round.view import RoundView

from Match.controller import MatchController


class TestDatabaseController(unittest.TestCase):
    t_p = TestPlayerModel()
    t_c = TournamentController(TournamentView)
    t_r = RoundController(RoundView)
    t_m = MatchController()

    def add_player(self):
        players = self.t_p.create_player()
        for p in players:
            p = serialize_player(p)
            print(p)
            players_table.insert(p)
        assert players_table

    def add_tournament(self):
        all_players = deserialized_every_players(players_table.all())
        new_test_tournament = self.t_c.create_tournament(all_players=all_players)
        new_first_round = self.t_r.generate_round(tournament=new_test_tournament)
        new_test_tournament.rounds.append(new_first_round)

        new_serialized_round = [serialize_round(new_test_tournament.rounds[0])]
        new_serialize_tournament = serialize_tournament(new_test_tournament, new_serialized_round)
        tournament_table.insert(new_serialize_tournament)
        assert tournament_table

    def evaluate_match(self):

        every_serialized_tournaments = tournament_table.all()
        deserialized_tournaments = []

        for tournament_serialized in every_serialized_tournaments:
            deserialized_t_players = deserialized_every_players(tournament_serialized['players_list'])

            current_deserialize_tournament = deserialize_tournament(tournament_serialized)

            current_deserialize_tournament.players_list = deserialized_t_players

            deserialized_tournaments.append(current_deserialize_tournament)

        self.t_m.evaluate_match(deserialized_tournaments[0].rounds[0]['match_history'][3],
                                deserialized_tournaments[0])
        s_tournament = serialize_tournament(deserialized_tournaments[0], deserialized_tournaments[0].rounds)
        s_tournament['players_list'] = serialize_tournament_players(s_tournament['players_list'])
        tournament_doc = tournament_table.get(doc_id=0 + 1)

        tournament_table.upsert(tinydb.database.Document(s_tournament, doc_id=tournament_doc.doc_id))
