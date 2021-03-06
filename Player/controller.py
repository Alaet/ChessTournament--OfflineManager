from .model import Player
from .serialize import serialize_player


class PlayerController:
    def __init__(self, view, last_player_id):
        self.view = view
        self.player_id = last_player_id

    def create_player(self):
        """
        Prompt for player info and return them as object Player
        :return: object(Player)
        """
        self.player_id += 1
        name = self.view.prompt_for_player_name()
        if name == "0":
            return None
        lastname = self.view.prompt_for_player_lastname()
        gender = self.view.prompt_for_player_gender()
        birthdate = self.view.prompt_for_player_birthdate()
        rank = self.view.prompt_for_player_rank()
        new_player_id = self.player_id
        score = 0
        new_player = Player(name, lastname, birthdate, gender, rank, new_player_id, score)
        serialized_player = serialize_player(new_player)

        return serialized_player

    def update_rank(self, tournament_players):
        """
        Prompt for updated players list rank, then update object(Player) self.rank based on input
        :param tournament_players:
        :return:
        """
        for player in tournament_players:
            self.view.display_new_player_rank(player)
            player.update_rank(self.view.prompt_for_new_rank())

    @staticmethod
    def reset_score(all_players):
        """
        Reset every players.score to 0
        :param all_players: list(object(Player))
        :return:
        """
        for player in all_players:
            player.score = 0
