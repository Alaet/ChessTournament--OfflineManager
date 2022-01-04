from .model import Match


def serialize_matches(matches):
    """
    Transform every object(Match) in list(dict{match_datas})
    :param matches: list(object(Match))
    :return: list(dict{match_datas})
    """
    serialized_matches = []
    for match in matches:
        serialized_match = {
            'match_info': match.match_info,
            'evaluated': match.evaluated
        }
        serialized_matches.append(serialized_match)
    return serialized_matches


def deserialize_matches(matches):
    """
    Transform every dict{match_datas} in list(object(Match))
    :param matches: list(dict{match_datas})
    :return: list(object(Match))
    """
    deserialized_matches = []
    for x, match in enumerate(matches):
        match_info = match['match_info']
        evaluated = match['evaluated']
        current_deserialize_match = Match(match_info, evaluated)
        deserialized_matches.append(current_deserialize_match)
    return deserialized_matches
