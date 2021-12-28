from .model import Player
from .serialize import serialize_player


class PlayerController(object):

    def __init__(self, view):
        self.view = view
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
        new_player_id = self.player_id
        score = 0
        new_player = Player(name, lastname, birthdate, gender, rank, score, player_id=new_player_id)
        serialized_player = serialize_player(new_player)

        return serialized_player

    def update_rank(self, tournament_players):
        for player in tournament_players:
            self.view.display_new_player_rank(player)
            player.update_rank(self.view.prompt_for_new_rank())
