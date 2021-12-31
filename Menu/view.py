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

    @staticmethod
    def display_tournaments(all_tournaments):
        """
        Display all tournaments existing
        :param all_tournaments: list(all_tournaments)
        :return: user tournament choice - tournament_choice
        """
        index = 1
        print("Pour quel tournoi ?    ( 0 - Menu principal )")
        for tournament in all_tournaments:
            print(str(index) + " . " + str(tournament.name) + "\n")
            index += 1
        tournament_choice = input()
        return tournament_choice

    @staticmethod
    def display_rounds(current_tournament):
        """
        Display all rounds existing
        :param current_tournament: object(Tournament)
        :return: user round choice - round_choice
        """
        print("Quel round ?    ( 0 - Menu principal )")
        for x, current_round in enumerate(current_tournament.rounds):
            print(str(current_round['round_name']) + "\n")
        round_choice = input()
        return round_choice

    @staticmethod
    def display_matches(match_list):
        """
        Display all match existing
        :param match_list: list(match)
        :return: user match choice - match_choice
        """

        print("Quel match ?    ( 0 - Menu principal )")
        for x, match in enumerate(match_list):
            if match['evaluated']:
                print(str(x+1) + ".Match terminé\n")
            else:
                print(str(x+1) + "." + str(match['match_info'][0][0]['name']) + " contre " +
                      str(match['match_info'][1][0]['name']) + "\n")
        match_choice = input()
        return match_choice

    def prompt_for_match_detail(self, all_t_list):
        """
        Prompt for tournament/round/match choices and return as int : [t_choice, r_choice, m_choice]
        :param all_t_list: list(all_tournaments)
        :return: [tournament_choice, round_choice, match_choice]
        """
        main_menu = [-1, -1, -1]
        try:

            t_choice = self.display_tournaments(all_t_list)
            if all_t_list[int(t_choice) - 1].close:
                print("Tournoi TERMINE")
                return main_menu
            if str(t_choice) == "0":
                return main_menu
            while not (t_choice.isnumeric()) and not (t_choice == ""):
                self.display_invalid_choice()
                t_choice = self.display_tournaments(all_t_list)
            t_choice = int(t_choice)

            r_choice = self.display_rounds(all_t_list[t_choice - 1])
            if str(r_choice) == "0":
                return main_menu
            while not (r_choice.isnumeric()) and not (r_choice == ""):
                self.display_invalid_choice()
                r_choice = self.display_rounds(all_t_list[t_choice - 1])
            r_choice = int(r_choice)

            m_choice = self.display_matches(all_t_list[t_choice - 1].rounds[r_choice - 1]['match_history'])
            if not all_t_list[t_choice - 1].rounds[r_choice - 1]['match_history'][int(m_choice) - 1]['evaluated']:
                if str(m_choice) == "0":
                    return main_menu
                while not (m_choice.isnumeric()) and not (m_choice == ""):
                    self.display_invalid_choice()
                    m_choice = self.display_matches(all_t_list[t_choice - 1].rounds[r_choice - 1]['match_history'])
                m_choice = int(m_choice)
                return [t_choice - 1, r_choice - 1, m_choice - 1]
            else:
                print("\n\nMatch terminé, veuillez en choisir un autre\n\n")
                return main_menu

        except IndexError:
            self.display_invalid_choice()
            return main_menu

    @staticmethod
    def missing_player_error():
        print("\n\n!!!!!!!!!!!!!!!! Veuillez créer au préalable "
              "des joueurs via le menu !!!!!!!!!!!!!!!!\n\n")

    @staticmethod
    def display_invalid_choice():
        print("\n\nChoix invalide\n\n")

    @staticmethod
    def display_all_tournaments(all_tournaments):
        for x, t in enumerate(all_tournaments):
            print(str(all_tournaments.index(all_tournaments[x])) + " - " + t.name + "   / Date de début : " + t.date)

    @staticmethod
    def display_all_players(all_players):
        print("Afficher par ordre alphabétique - N\n")
        print("Afficher par rang - R\n")

        sorting_choice = type(input)
        while sorting_choice != "N" or sorting_choice != "R":
            sorting_choice = input()
            if sorting_choice == "N":
                sorted_by_name = sorted(all_players, key=lambda x: x.name)
                for player in sorted_by_name:

                    print("ID : " + str(player.id) + " - Nom : " + player.name + " - Rang : " + str(player.rank) +
                          "\n")
                print("\n(Selectionner un joueur via son ID pour mettre à jour son rang,\n\"Entrée\" pour passer)")
                break
            elif sorting_choice == "R":
                sorted_by_rank = sorted(all_players, key=lambda x: x.rank)
                for player in sorted_by_rank:

                    print("ID : " + str(player.id) + " - Rang : " + str(player.rank) + " - Nom : " + player.name +
                          "\n")
                print("\n(Selectionner un joueur via son ID pour mettre à jour son rang,\n\"Entrée\" pour passer)")
                break
            else:
                View.display_invalid_choice()
