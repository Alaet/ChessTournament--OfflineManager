def serialize_player(new_player):
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
