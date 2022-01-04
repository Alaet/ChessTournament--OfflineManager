from .model import Tournament
from Player.serialize import deserialized_every_players


def serialize_tournament(new_tournament, current_round):
    """
    Transform an object(Tournament) in dict
    :param new_tournament: object(Tournament)
    :param current_round: object(Round)
    :return: dict{tournament_datas}
    """
    serialized_tournament = {
        'name': new_tournament.name,
        'place': new_tournament.place,
        'date': new_tournament.date,
        'time_mode': new_tournament.time_mode,
        'match_count': new_tournament.match_count,
        'round_count': new_tournament.round_count,
        'players_list': new_tournament.players_list,
        'description': new_tournament.description,
        'rounds': current_round,
        'close': new_tournament.close
    }
    return serialized_tournament


def deserialize_tournament(new_tournament):
    """
    Transform a dict{tournament_datas} in object(Tournament)
    :param new_tournament: dict{tournament_datas}
    :return: object(Tournament)
    """
    name = new_tournament['name']
    place = new_tournament['place']
    date = new_tournament['date']
    time_mode = new_tournament['time_mode']
    players_list = deserialized_every_players(new_tournament['players_list'])
    description = new_tournament['description']
    rounds = new_tournament['rounds']
    deserialized_tournament = Tournament(name, place, date, time_mode, players_list, description)
    deserialized_tournament.rounds = rounds
    deserialized_tournament.match_count = new_tournament['match_count']
    deserialized_tournament.round_count = new_tournament['round_count']
    deserialized_tournament.round_count = new_tournament.get('round_count', '')
    deserialized_tournament.close = new_tournament['close']

    return deserialized_tournament


def serialize_tournament_players(tournament_player):
    """
    Transform every object(Player) for a given tournament in list(dict{players_data})
    :param tournament_player: list(object(Player))
    :return: list(dict{players_data})
    """
    serialized_players = []
    for player in tournament_player:
        serialized_players.append({
            'name': player.name,
            'lastname': player.lastname,
            'birthdate': player.birthdate,
            'gender': player.gender,
            'rank': player.rank,
            'id': player.id,
            'score': player.score
        })
    return serialized_players
