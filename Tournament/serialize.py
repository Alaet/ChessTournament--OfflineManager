from .model import Tournament
from Player.model import Player
from Round.serialize import deserialize_all_rounds


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
        'rounds': current_round
    }
    return serialized_tournament


def deserialize_tournament(new_tournament):

    name = new_tournament['name']
    place = new_tournament['place']
    date = new_tournament['date']
    time_mode = new_tournament['time_mode']
    players_list = deserialized_tournament_players(new_tournament['players_list'])
    description = new_tournament['description']
    rounds = new_tournament['rounds']
    deserialized_tournament = Tournament(name, place, date, time_mode, players_list, description)
    deserialized_tournament.rounds = rounds
    deserialized_tournament.match_count = new_tournament['match_count']
    deserialized_tournament.round_count = new_tournament['round_count']

    return deserialized_tournament


def deserialized_tournament_players(serialized_player):
    all_players = []
    for x, player in enumerate(serialized_player):
        name = serialized_player[x]['name']
        lastname = serialized_player[x]['lastname']
        birthdate = serialized_player[x]['birthdate']
        gender = serialized_player[x]['gender']
        rank = serialized_player[x]['rank']
        id_deserialized = x
        score = serialized_player[x]['score']
        deserialized_player = Player(name=name, lastname=lastname, birthdate=birthdate, gender=gender,
                                     rank=rank, player_id=id_deserialized, score=score)
        all_players.append(deserialized_player)
    return all_players


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


def deserialize_all_tournament(all_tournament_serialized):
    all_tournament_deserialized = []

    for x, tournament in enumerate(all_tournament_serialized):
        name = all_tournament_serialized[x]['name']
        place = all_tournament_serialized[x]['place']
        date = all_tournament_serialized[x]['date']
        time_mode = all_tournament_serialized[x]['time_mode']
        players_list = deserialized_tournament_players(all_tournament_serialized[x]['players_list'])
        description = all_tournament_serialized[x]['description']
        deserialized_tournament = Tournament(name, place, date, time_mode, players_list, description)

        deserialized_rounds = deserialize_all_rounds(all_tournament_serialized[x]['rounds'])
        deserialized_tournament.rounds.append(deserialized_rounds)
        deserialized_tournament.match_count = all_tournament_serialized[x]['match_count']
        deserialized_tournament.round_count = all_tournament_serialized[x]['round_count']

        all_tournament_deserialized.append(deserialized_tournament)
    return all_tournament_deserialized
