from Match.serialize import serialize_matches


def serialize_round(new_round):
    serialized_round = {
        'round_name': new_round.round_name,
        'round_starting_date': new_round.round_starting_date,
        'round_ending_date': new_round.round_ending_date,
        'match_history': serialize_matches(new_round.match_history)
    }
    return serialized_round
