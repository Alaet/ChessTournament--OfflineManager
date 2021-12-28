from .model import Round
from Match.serialize import deserialize_matches, serialize_matches


def serialize_round(new_round):
    serialized_round = {
        'round_name': new_round.round_name,
        'round_starting_date': new_round.round_starting_date,
        'round_ending_date': new_round.round_ending_date,
        'match_history': serialize_matches(new_round.match_history)
    }
    return serialized_round


def serialize_all_rounds(rounds):
    all_rounds_serialized = []
    for round in rounds:
        serial_round = {
            'round_name': round.round_name,
            'round_starting_date': round.round_starting_date,
            'round_ending_date': round.round_ending_date,
            'match_history': serialize_matches(round.match_history)
        }
        all_rounds_serialized.append(serial_round)
    return all_rounds_serialized


def deserialize_round(serialize_round, round_serialized_matches):
    round_name = serialize_round['round_name']
    round_starting_date = serialize_round['round_starting_date']
    round_ending_date = serialize_round['round_ending_date']

    round_deserialize_matches = deserialize_matches(round_serialized_matches)
    deserialized_round = Round(round_deserialize_matches)
    deserialized_round.round_name = round_name
    deserialized_round.round_starting_date = round_starting_date
    deserialized_round.round_ending_date = round_ending_date
    return deserialized_round


def deserialize_all_rounds(serialize_rounds):
    all_serialized_rounds = []

    for s_round in serialize_rounds:
        round_name = s_round['round_name']
        round_starting_date = s_round['round_starting_date']
        round_ending_date = s_round['round_ending_date']

        round_deserialized_matches = deserialize_matches(s_round['match_history'])
        deserialized_round = Round(round_deserialized_matches)
        deserialized_round.round_name = round_name
        deserialized_round.round_starting_date = round_starting_date
        deserialized_round.round_ending_date = round_ending_date
        all_serialized_rounds.append(deserialized_round)

    return all_serialized_rounds
