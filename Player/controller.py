from .model import Player


class PlayerController(object):

    def __init__(self, view):
        self.view = view
        self.model = object
        self.player_id = -1

    def create_player(self):
        """
        prompt for player info and return them as object Player
        :return: object(Player)
        """
        self.player_id += 1
        name = self.view.prompt_for_player_name()
        if name == "0":
            return None
        rank = self.view.prompt_for_player_rank()
        lastname = self.view.prompt_for_player_lastname()
        gender = self.view.prompt_for_player_gender()
        birthdate = self.view.prompt_for_player_birthdate()
        id = self.player_id
        new_player = Player(name, lastname, birthdate, gender, rank, id)
        return new_player

    def update_rank(self, tournament_players):
        for player in tournament_players:
            player.update_rank(self.view.prompt_for_new_rank())
