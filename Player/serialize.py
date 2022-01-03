from .model import Player


def serialize_player(new_player):
    """
    Transform an object(Player) in dict{player_datas}
    :param new_player: object(Player)
    :return: dict{player_datas}
    """
    serialized_player = {
        'name': new_player.name,
        'lastname': new_player.lastname,
        'birthdate': new_player.birthdate,
        'gender': new_player.gender,
        'rank': new_player.rank,
        'id': new_player.id,
        'score': new_player.score
    }
    return serialized_player


def deserialized_every_players(serialized_player):
    """
    Transform every dict{player_datas} in list(object(Player))
    :param serialized_player: list(list(object(Player)))
    :return: list(object(Player))
    """
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
