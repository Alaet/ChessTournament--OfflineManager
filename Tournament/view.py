class TournamentView:

    def __init__(self):
        self.menu_options_tournament = ["1. Liste de tous les joueurs", "2. Liste de tous les tours",
                                        "3. Liste de tous les matches"]

    def display_tournament_rounds(self, tournament):
        for round in tournament.rounds:
            print(round.round_name + " - " + round.match_history[0].match_info[0][0].name + " contre " +
                  round.match_history[0].match_info[1][0].name + "\n")
        input()

    def display_tournament_matches(self, tournament):
        for round in tournament.rounds:
            for match in round.match_history:
                print(match.match_info[0][0].name + " contre " + match.match_info[1][
                    0].name + "\n")
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
        picked_player = []
        for player in all_players:
            print(str(player.id) + ".  " + player.name)
        while x < 8:
            choice = input()
            for player in all_players:
                if choice == str(player.id):
                    picked_player.append(player)
                    x += 1
                elif not choice.isnumeric() or choice == "":
                    print("Id non reconnu")
                else:
                    print("Id non reconnu")

        return picked_player

    @staticmethod
    def prompt_for_tournament_name():

        name = input("Entrez le nom du tournoi    ( 0 - Menu principal )\n")
        while not name.isalpha() or name == "":
            print("Le format du nom n'est pas reconnu")
            name = input("Entrez le nom du tournoi    ( 0 - Menu principal )\n")
            if name == "0":
                break
        return name

    @staticmethod
    def prompt_for_tournament_place():

        place = input("Entrez le lieu du tournoi\n")
        while not place.isalpha():
            print("Le format du nom du lieu n'est pas reconnu")
            place = input("Entrez le lieu du tournoi\n")
            if place == "0":
                break
        return place

    @staticmethod
    def prompt_for_tournament_date():
        import dateutil.parser
        is_date_valid = False

        while not is_date_valid:
            birthdate = input("Entrez la date du tournoi (au format JJ/MM/YYYY)\n")
            try:
                if 7 <= len(birthdate) <= 10:

                    birthdate = dateutil.parser.parse(birthdate, dayfirst=True)
                    birthdate = birthdate.strftime('%d-%m-%Y')
                    is_date_valid = True
                else:
                    print("Le format de la date du tournoi n'est pas reconnue")
            except dateutil.parser.ParserError:
                print("Le format de la date du tournoi n'est pas reconnue")

        return birthdate

    @staticmethod
    def prompt_for_time_mode():

        time_mode = type(input)
        print("Entrez le type de partie    ( 0 - Menu principal )\nBullet : Bul\nBlitz : Bli\nCoup rapide : Cra\n")
        while not time_mode == "Bul" or not time_mode == "Bli" or not time_mode == "Cra":
            time_mode = input()
            if time_mode == "Bul":
                return time_mode
            elif time_mode == "Bli":
                return time_mode
            elif time_mode == "Cra":
                return time_mode
            elif time_mode == "0":
                break
            else:
                print("Format non reconnu")
        return time_mode

    @staticmethod
    def prompt_for_description():
        description = input("Ajouter un commentaire sur le tournoi :\n\n")
        return description
