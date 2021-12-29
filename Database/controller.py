import tinydb as tinydb
from tinydb import TinyDB, Query
from Player.serialize import serialize_player
from Tournament.serialize import deserialized_every_players, deserialize_tournament

db = TinyDB('db.json', indent=4)
players_table = db.table('players')
tournament_table = db.table('tournaments')


def insert_player(new_player_to_add):
    players_table.insert(new_player_to_add)


def insert_tournament(new_tournament_to_add):
    tournament_table.insert(new_tournament_to_add)


def update_players_rank(players_list):
    for x, player in enumerate(players_list):
        User = Query()
        db_player_update = serialize_player(player)
        players_table.upsert(db_player_update, User.name == str(player.name))


def get_all_players():
    return players_table.all()


def get_all_tournaments():
    return tournament_table.all()


def deserialize_all_tournaments(every_serialized_tournaments):
    deserialized_tournaments = []

    for tournament_serialized in every_serialized_tournaments:
        deserialized_t_players = deserialized_every_players(tournament_serialized['players_list'])

        current_deserialize_tournament = deserialize_tournament(tournament_serialized)

        current_deserialize_tournament.players_list = deserialized_t_players

        deserialized_tournaments.append(current_deserialize_tournament)
    return deserialized_tournaments


def update_tournament(s_tournament, tournament_index):
    tournament_doc = tournament_table.get(doc_id=tournament_index + 1)
    tournament_table.upsert(tinydb.database.Document(s_tournament, doc_id=tournament_doc.doc_id))
