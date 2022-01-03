class PlayerView:

    @staticmethod
    def prompt_for_player_name():
        """
        Prompt for a name
        :return: str
        """

        name = input("\n\nEntrez le prénom du joueur    ( 0 - Menu principal )\n")

        while not name.isalpha() and not name == "0":
            print("\n\nLe format du prénom n'est pas reconnu\n\n")
            name = input("\n\nEntrez le prénom du joueur    ( 0 - Menu principal )\n")
            if name == "0":
                break
        return name

    @staticmethod
    def prompt_for_player_lastname():
        """
        Prompt for a lastname
        :return: str
        """

        lastname = input("\n\nEntrez le nom du joueur\n")
        while not lastname.isalpha():
            print("\n\nLe format du nom n'est pas reconnu\n\n")
            lastname = input("\n\nEntrez le nom du joueur\n")
        return lastname

    @staticmethod
    def prompt_for_player_gender():
        """
        prompt_for_player_gender
        :return: str
        """

        gender = input("Entrez le genre : Male / Female\n")
        while not (gender == "Female" or gender == "F") and not (gender == "Male" or gender == "M"):
            print("Le format du genre n'est pas reconnu")
            gender = input("Entrez le genre : Male / Female\n")
        return gender

    @staticmethod
    def prompt_for_player_rank():
        """
        prompt_for_player_rank
        :return: int
        """

        rank = input("Entrez le rang actuel\n")
        while not rank.isnumeric() or rank == "" or rank == "0":
            print("\n\nLe format du rang n'est pas reconnu\n\n")
            rank = input("Entrez le rang actuel\n")
        return int(rank)

    @staticmethod
    def prompt_for_player_birthdate():
        """
        prompt_for_player_birthdate
        :return: str
        """

        is_date_valid = False
        birthdate = None
        while not is_date_valid:
            import dateutil.parser
            birthdate = input("Entrez la date de naissance (au format JJ/MM/YYYY)\n")
            try:
                if 7 <= len(birthdate) <= 10:

                    birthdate = dateutil.parser.parse(birthdate, dayfirst=True)
                    birthdate = birthdate.strftime('%d-%m-%Y')
                    is_date_valid = True
                else:
                    print("Le format de la date de naissance n'est pas reconnue")
            except dateutil.parser.ParserError:
                print("Le format de la date de naissance n'est pas reconnue")

        return birthdate

    @staticmethod
    def prompt_for_new_rank():
        """
        prompt_for_new_rank
        :return: int
        """
        new_rank = input()
        while new_rank == "0" or new_rank.isalpha() or new_rank == "":
            if new_rank == "0":
                print("Impossible de mettre le rang à 0")
                new_rank = input()
            elif new_rank.isalpha() or new_rank == "":
                print("Saisissez une valeur numérique")
                new_rank = input()
        return int(new_rank)

    @staticmethod
    def display_new_player_rank(player):
        print("\n*****************************\n")
        print("Ancien rang de " + player.name + " :  " + str(player.rank))
        print("Mettez à jour le rang : ")
