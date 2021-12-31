class TournamentView:

    def __init__(self):
        self.menu_options_tournament = ["1. Liste de tous les joueurs", "2. Liste de tous les tours",
                                        "3. Liste de tous les matches"]

    @staticmethod
    def display_tournament_matches(tournament):
        """
        Display every match for every round for given tournament in parameter
        :param tournament: dict(tournament_data)
        :return:
        """
        for current_round in tournament.rounds:
            print(current_round['round_name'] + " ")
            for match in current_round['match_history']:
                print(match['match_info'][0][0]['name'] + " contre " + match['match_info'][1][0]['name'])
                print("score : " + str(match['match_info'][0][0]['score']) + " / " + str(match[
                    'match_info'][1][0]['score']) + "\n")
        input()

    def display_tournament_option_menu(self):
        """
        Dsplay tournament menu option
        :return: user choice
        """
        for option in self.menu_options_tournament:
            print(option)
        choice = input()
        while choice != "1" and not "2" and not "3" or not "0" and not "":
            print("Choix invalide")
            choice = input()

        return choice

    @staticmethod
    def pick_players_for_tournament(all_players):
        """
        Take all_players from list of object(Player) as parameter
        and return 8 object(Player) as list
        :param all_players: list(object(Player)
        :return: list(object(Player))
        """
        x = 0
        good = False
        picked_player = []
        for player in all_players:
            print(str(player.id) + ".  " + player.name)
        while not good:
            old_len = len(picked_player)
            if x == 8:
                good = True
                break
            choice = input()
            if x < 8:
                for player in all_players:
                    if choice == str(player.id):
                        picked_player.append(player)
                        all_players.remove(player)
                        print("Joueur " + str(x+1) + " : " + player.name
                              + " ajouté au tournoi")
                        x += 1
                for player in all_players:
                    print(str(player.id) + ".  " + player.name)
                if len(picked_player) == old_len:
                    print("Id non reconnu")

        return picked_player

    @staticmethod
    def prompt_for_tournament_name():
        """
        Prompt for tournament name, break to main menu
        :return: str(tournament_name)
        """

        name = input("Entrez le nom du tournoi    ( 0 - Menu principal )\n")
        while not name.isalpha() or name == "":
            print("Le format du nom n'est pas reconnu\n")
            name = input("Entrez le nom du tournoi    ( 0 - Menu principal )\n")
            if name == "0":
                break
        return name

    @staticmethod
    def prompt_for_tournament_place():
        """
        Prompt for tournament place, break to main menu
        :return: str(tournament_place)
        """

        place = input("Entrez le lieu du tournoi\n")
        while not place.isalpha():
            print("Le format du nom du lieu n'est pas reconnu\n")
            place = input("Entrez le lieu du tournoi\n")
            if place == "0":
                break
        return place

    @staticmethod
    def prompt_for_tournament_date():
        """
        Prompt for tournament date, break to main menu
        :return: str(tournament_date)
        """
        import dateutil.parser
        is_date_valid = False
        tournament_date = []
        while not is_date_valid:
            tournament_date = input("Entrez la date du tournoi (au format JJ/MM/YYYY)\n")
            try:
                if 7 <= len(tournament_date) <= 10:

                    tournament_date = dateutil.parser.parse(tournament_date, dayfirst=True)
                    tournament_date = tournament_date.strftime('%d-%m-%Y')
                    is_date_valid = True
                else:
                    print("Le format de la date du tournoi n'est pas reconnue\n")
            except dateutil.parser.ParserError:
                print("Le format de la date du tournoi n'est pas reconnue\n")

        return tournament_date

    @staticmethod
    def prompt_for_time_mode():
        """
        Prompt for tournament date, break to main menu
        :return: str(int(time_mode))
        """
        time_mode = type(input)
        print("Entrez le type de partie    ( 0 - Menu principal )\n1. Bullet\n2. Blitz\n3. Coup rapide\n")
        while not time_mode == "1" and not time_mode == "2" and not time_mode == "3":
            time_mode = input()
            if time_mode == "1":
                return time_mode
            elif time_mode == "2":
                return time_mode
            elif time_mode == "3":
                return time_mode
            elif time_mode == "0":
                break
            else:
                print("Format non reconnu\n")
        return time_mode

    @staticmethod
    def prompt_for_description():
        """
        Prompt for tournament date, break to main menu
        :return: str(tournament_description)
        """
        description = input("Ajouter un commentaire sur le tournoi :\n\n")
        return description
