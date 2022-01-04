import tinydb as tinydb
from tinydb import TinyDB, Query
from Player.serialize import serialize_player, deserialized_every_players
from Tournament.serialize import deserialize_tournament

db = TinyDB('db.json', indent=4)
players_table = db.table('players')
tournament_table = db.table('tournaments')


def insert_player(new_player_to_add):
    """
    Add new player to database
    :param new_player_to_add: serialized_object(Player)
    :return:
    """
    players_table.insert(new_player_to_add)


def insert_tournament(new_tournament_to_add):
    """
    Add new tournament to database
    :param new_tournament_to_add: serialized_object(Tournament)
    :return:
    """
    tournament_table.insert(new_tournament_to_add)


def update_players_rank(players_list):
    """
    Update players rank retrieved from user input towards player datas inside Database
    :param players_list: list(object(Player))
    :return:
    """
    for x, player in enumerate(players_list):
        User = Query()
        db_player_update = serialize_player(player)
        players_table.upsert(db_player_update, User.name == str(player.name))


def get_all_players():
    """
    Get all players registered in database
    :return: list(dict{players_datas})
    """
    return players_table.all()


def get_all_tournaments():
    """
    Get all tournaments registered in database
    :return: list(dict{tournament_datas})
    """
    return tournament_table.all()


def deserialize_all_tournaments():
    """
    Transform every serialized tournament registered in database in an object(Tournament)
    :return: list(object(Tournament))
    """
    every_serialized_tournaments = get_all_tournaments()
    deserialized_tournaments = []

    for tournament_serialized in every_serialized_tournaments:
        deserialized_t_players = deserialized_every_players(tournament_serialized['players_list'])

        current_deserialize_tournament = deserialize_tournament(tournament_serialized)

        current_deserialize_tournament.players_list = deserialized_t_players

        deserialized_tournaments.append(current_deserialize_tournament)
    return deserialized_tournaments


def update_tournament(s_tournament, tournament_index):
    """
    Update tournament datas towards Database
    :param s_tournament: serialized_object(Tournament)
    :param tournament_index: int
    :return:
    """
    tournament_doc = tournament_table.get(doc_id=tournament_index + 1)
    tournament_table.upsert(tinydb.database.Document(s_tournament, doc_id=tournament_doc.doc_id))


def last_player_id():
    """
    Get index from last player in every player registered in database minus one
    :return: int
    """
    return len(get_all_players()) - 1
