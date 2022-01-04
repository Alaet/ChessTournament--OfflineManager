class Player:

    def __init__(self, name, lastname, birthdate, gender, rank, player_id, score=int):
        self.name = name
        self.lastname = lastname
        self.birthdate = birthdate
        self.gender = gender
        self.rank = rank
        self.id = player_id
        self.score = score

    def __str__(self):
        return "ID : " + str(self.id) + " - Nom : " + self.name + " - Rang : " + str(self.rank) + "\n"

    def add_score(self, points):
        """
        add score to player
        :param points: int(point_to_add)
        :return: updated self.score
        """
        self.score += points

    def update_rank(self, new_rank):
        """
        Get new rank set by user and update self.rank with new rank if int(input()) in parameter != 0
        :param new_rank: int(input())
        :return:
        """
        if new_rank != 0:
            self.rank = new_rank
