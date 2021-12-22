class Player(object):

    def __init__(self, name, lastname, birthdate, gender, rank, id):
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.id = id
        self.score: float = 0

    def add_score(self, points):
        """
        add score to player
        :param points: int(point_to_add)
        :return: updated self.score
        """
        self.score += points
