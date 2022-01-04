class RoundView:

    @staticmethod
    def display_tournament_rounds(tournament):
        """
        Display every round and starting/ending date for given tournament in parameter
        :param tournament: dict(tournament_data)
        :return:
        """
        for current_round in tournament.rounds:
            print(current_round['round_name'] + "\n" + "Début : " + str(
                current_round['round_starting_date']) + "\n" + "Fin   : " + str(current_round['round_ending_date']))
        input()
