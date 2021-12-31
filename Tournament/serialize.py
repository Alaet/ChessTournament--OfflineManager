from .model import Tournament
from Player.model import Player


def serialize_tournament(new_tournament, current_round):
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


def deserialized_every_players(serialized_player):
    all_players_deserialized = []
    for x, player in enumerate(serialized_player):
        name = serialized_player[x]['name']
        lastname = serialized_player[x]['lastname']
        birthdate = serialized_player[x]['birthdate']
        gender = serialized_player[x]['gender']
        rank = serialized_player[x]['rank']
        id_deserialized = serialized_player[x]['id']
        score = serialized_player[x]['score']
        deserialized_player = Player(name=name, lastname=lastname, birthdate=birthdate, gender=gender,
                                     rank=rank, player_id=id_deserialized, score=score)
        all_players_deserialized.append(deserialized_player)
    return all_players_deserialized


def serialize_tournament_players(tournament_player):
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
