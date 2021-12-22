class View:

    def __init__(self):

        self.main_menu_options = ["1. Créer Joueur", "2. Créer tournoi", "3. Entrée les résultats d'un match",
                                  "4. Rapports", "0. Quitter programme"]
        self.menu_options_data_base = ["1. Liste de tous les joueurs", "2. Liste de tous les tournois"]

    def display_reports_menu(self):
        """
        Dsplay main report menu option
        :return: user choice
        """
        print("*************************************\n\n")
        for option in self.menu_options_data_base:
            print(option)
        choice = input()
        while choice != "1" and not "2" or not "0" and not "":
            self.display_invalid_choice()
            choice = input()

        return choice

    def display_main_menu(self):
        """
        Dsplay main menu option
        :return: user choice
        """

        for option in self.main_menu_options:
            print(option)
        choice = input()
        while choice != "1" and not "2" or not "3" or not "4" or not "0" and not "":
            self.display_invalid_choice()
            choice = input()

        return choice

    def display_tournaments(self, tournaments):
        """
        Display all tournaments existing
        :param tournaments: list(all_tournaments)
        :return: user tournament choice - tournament_choice
        """
        tournament_index = 1
        print("Pour quel tournoi ?    ( 0 - Menu principal )")
        for tournament in tournaments:
            print(str(tournament_index) + " . " + str(tournament.name) + "\n")
            tournament_index += 1
        tournament_choice = input()
        return tournament_choice

    def display_rounds(self, tournament):
        """
        Display all rounds existing
        :param tournament: object(Tournament)
        :return: user round choice - round_choice
        """
        print("Quel round ?    ( 0 - Menu principal )")
        for round in tournament.rounds:
            print(str(round.round_name) + "\n")
        round_choice = input()
        return round_choice

    def display_matches(self, matches):
        """
        Display all match existing
        :param matches: list(match)
        :return: user match choice - match_choice
        """

        print("Quel match ?    ( 0 - Menu principal )")

        for x, match in enumerate(matches):
            if match.evaluated:
                print(str(x+1) + ".Match terminé\n")
            else:
                print(str(x+1) + "." + str(match.match_info[0][0].name) + " contre " +
                      str(match.match_info[1][0].name) + "\n")
        match_choice = input()
        return match_choice

    def prompt_for_match_detail(self, tournaments):
        """
        Prompt for tournament/round/match choices and return as int : [t_choice, r_choice, m_choice]
        :param tournaments: list(all_tournaments)
        :return: [tournament_choice, round_choice, match_choice]
        """

        main_menu = [-1, -1, -1]
        try:

            choice = self.display_tournaments(tournaments)
            if tournaments[int(choice) - 1].close:
                print("Tournoi TERMINE")
                return main_menu
            if str(choice) == "0":
                return main_menu
            while not (choice.isnumeric()) and not (choice == ""):
                self.display_invalid_choice()
                choice = self.display_tournaments(tournaments)
            choice = int(choice)

            round_choice = self.display_rounds(tournaments[choice - 1])
            if str(round_choice) == "0":
                return main_menu
            while not (round_choice.isnumeric()) and not (choice == ""):
                self.display_invalid_choice()
                round_choice = self.display_rounds(tournaments[choice - 1])
            round_choice = int(round_choice)

            match_choice = self.display_matches(tournaments[choice - 1].rounds[round_choice - 1].match_history)
            if not tournaments[choice - 1].rounds[round_choice - 1].match_history[int(match_choice) - 1].evaluated:
                if str(match_choice) == "0":
                    return main_menu
                while not (match_choice.isnumeric()) and not (choice == ""):
                    self.display_invalid_choice()
                    match_choice = self.display_matches(tournaments[choice - 1].rounds[round_choice - 1].match_history)
                match_choice = int(match_choice)
                return [choice - 1, round_choice - 1, match_choice - 1]
            else:
                print("\n\nMatch terminé, veuillez en choisir un autre\n\n")
                return main_menu

        except IndexError:
            self.display_invalid_choice()
            return main_menu

    def missing_player_error(self):
        print("\n\n!!!!!!!!!!!!!!!! Veuillez créer au préalable "
              "des joueurs via le menu !!!!!!!!!!!!!!!!\n\n")

    def display_invalid_choice(self):
        print("\n\nChoix invalide\n\n")

    def display_all_tournaments(self, all_tournaments):
        for x, t in enumerate(all_tournaments):
            print(str(all_tournaments.index(all_tournaments[x])) + " - " + t.name)

    def display_all_players(self, all_players):
        print("Afficher par ordre alphabétique - N\n")
        print("Afficher par rang - R\n")
        choice = type(input)
        while choice != "N" or choice != "R":
            choice = input()
            if choice == "N":
                sorted_by_name = sorted(all_players, key=lambda x: x.name)
                for player in sorted_by_name:
                    print("Nom :" + player.name + " - Rang :" + str(player.rank) + "\n")
                break
            elif choice == "R":
                sorted_by_rank = sorted(all_players, key=lambda x: x.rank)
                for player in sorted_by_rank:
                    print("Nom :" + player.name + " - Rang :" + str(player.rank) + "\n")
                break
            else:
                View.display_invalid_choice(self)
