class PlayerView:

    @staticmethod
    def prompt_for_player_name():

        name = input("\n\nEntrez le prénom du joueur    ( 0 - Menu principal )\n")

        while not name.isalpha() and not name == "0":
            print("\n\nLe format du prénom n'est pas reconnu\n\n")
            name = input("\n\nEntrez le prénom du joueur    ( 0 - Menu principal )\n")
            if name == "0":
                break

        return name

    @staticmethod
    def prompt_for_player_lastname():

        lastname = input("\n\nEntrez le nom du joueur\n")
        while not lastname.isalpha():
            print("\n\nLe format du nom n'est pas reconnu\n\n")
            lastname = input("\n\nEntrez le nom du joueur\n")

        return lastname

    @staticmethod
    def prompt_for_player_gender():

        gender = input("Entrez le genre : Male / Female\n")
        while not (gender == "Female" or gender == "F") and not (gender == "Male" or gender == "M"):
            print("Le format du genre n'est pas reconnu")
            gender = input("Entrez le genre : Male / Female\n")

        return gender

    @staticmethod
    def prompt_for_player_rank():

        rank = input("Entrez le rang actuel\n")
        while not rank.isnumeric() or rank == "" or rank == "0":
            print("\n\nLe format du rang n'est pas reconnu\n\n")
            rank = input("Entrez le rang actuel\n")

        return int(rank)

    @staticmethod
    def prompt_for_player_birthdate():

        is_date_valid = False

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
