from .model import Tournament
from Player.model import Player


class TournamentController(object):

    def __init__(self, view):
        self.view = view

    def create_tournament(self, serialized_player):
        """
        Prompt for tournament details, and players from list(all_players) of object(Player) to pick
        to return an object(Tournament)
        :param serialized_player: TinyDB list(Document(Player_data))
        :return: object(Tournament)
        """
        all_players = self.deserialized_tournament_players(serialized_player)
        print(all_players)
        name = self.view.prompt_for_tournament_name()
        place = self.view.prompt_for_tournament_place()
        date = self.view.prompt_for_tournament_date()
        time_mode = self.view.prompt_for_time_mode()
        players = self.view.pick_players_for_tournament(all_players)
        description = self.view.prompt_for_description()
        new_tournament = Tournament(name, place, date, time_mode, players, description)
        return new_tournament

    @staticmethod
    def evaluate_match(match, tournament):
        """
        Prompt for winner from matched player then add score to this player
        and return match number index for this round
        :param match: tuple[(object(Player), player.score), (obect(Player), player.score)]
        :param tournament: object(Tournament)
        :return: int(tournament.match_count)
        """

        tournament.match_count += 1

        print("Match " + str(tournament.match_count) + "    ( 0 - Menu principal )\n1." + str(match.match_info[0][0]
                                                                                              .name) + "\n\n2."
              + str(match.match_info[1][0].name) + "\n3. Match nul")
        result = input()
        if result == "0":
            tournament.match_count -= 1
            return result
        elif result == "1":
            match.match_info[0][0].score += 1

        elif result == "2":
            match.match_info[1][0].score += 1

        elif result == "3":
            match.match_info[0][0].score += (1 / 2)
            match.match_info[1][0].score += (1 / 2)

        match.evaluated = True

        return tournament.match_count

    @staticmethod
    def cloture_round(round):

        if input("Clôturer le round ?  O/N\n") == "O" or "N":
            import datetime
            round.round_ending_date = datetime.datetime.now()
            round.round_ending_date = round.round_ending_date.strftime("%Y-%m-%d %H:%M:%S")
            print(round.round_ending_date)

    @staticmethod
    def reset_score(all_players):
        for player in all_players:
            player.score = 0

    @staticmethod
    def deserialized_tournament_players(serialized_player):
        all_players = []
        for x, player in enumerate(serialized_player):
            name = serialized_player[x]['name']
            lastname = serialized_player[x]['lastname']
            birthdate = serialized_player[x]['birthdate']
            gender = serialized_player[x]['gender']
            rank = serialized_player[x]['rank']
            id = x#serialized_player[x]['id']
            deserialized_player = Player(name=name, lastname=lastname, birthdate=birthdate, gender=gender,
                                         rank=rank, player_id=id)
            all_players.append(deserialized_player)
        return all_players
