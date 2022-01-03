# https://docs.python.org/fr/3/library/unittest.html
import unittest

import tinydb

from .db_test import players_table_test
from .db_test import tournament_table_test
from Database.controller import deserialize_tournament

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

    @staticmethod
    def add_player():
        players = TestPlayerModel.create_player()
        for p in players:
            print(p.name)
            p = serialize_player(p)
            players_table_test.insert(p)

    @staticmethod
    def add_tournament():
        all_players = deserialized_every_players(players_table_test.all())
        new_test_tournament = TournamentController.create_tournament(self=TournamentController(TournamentView),
                                                                     all_players=all_players)
        new_first_round = RoundController.generate_round(self=RoundController(RoundView),
                                                         tournament=new_test_tournament)
        new_test_tournament.rounds.append(new_first_round)

        new_serialized_round = [serialize_round(new_test_tournament.rounds[0])]
        new_serialize_tournament = serialize_tournament(new_test_tournament, new_serialized_round)
        tournament_table_test.insert(new_serialize_tournament)

    @staticmethod
    def evaluate_match():

        every_serialized_tournaments = tournament_table_test.all()
        deserialized_tournaments = []

        for tournament_serialized in every_serialized_tournaments:
            deserialized_t_players = deserialized_every_players(tournament_serialized['players_list'])

            current_deserialize_tournament = deserialize_tournament(tournament_serialized)

            current_deserialize_tournament.players_list = deserialized_t_players

            deserialized_tournaments.append(current_deserialize_tournament)

        MatchController.evaluate_match(deserialized_tournaments[0].rounds[0]['match_history'][3],
                                       deserialized_tournaments[0])
        s_tournament = serialize_tournament(deserialized_tournaments[0], deserialized_tournaments[0].rounds)
        s_tournament['players_list'] = serialize_tournament_players(s_tournament['players_list'])
        tournament_doc = tournament_table_test.get(doc_id=0 + 1)

        tournament_table_test.upsert(tinydb.database.Document(s_tournament, doc_id=tournament_doc.doc_id))
