class MatchController:

    @staticmethod
    def evaluate_match(match, tournament):
        """
        Prompt for winner from matched player then add score to this player
        and return match number index for this round
        :param match: tuple[(object(Player), player.score), (obect(Player), player.score)]
        :param tournament: object(Tournament)
        :return: int(tournament.match_count)
        """
        if tournament.match_count < 4:
            tournament.match_count += 1
        else:
            tournament.match_count = 1

        print("Match " + str(tournament.match_count) + "    ( 0 - Menu principal )\n1." + str(match['match_info'][0][0]
                                                                                              ['name']) + "\n\n2."
              + str(match['match_info'][1][0]['name']) + "\n3. Match nul")
        result = input()
        if result == "0":
            tournament.match_count -= 1
            return result
        elif result == "1":
            match['match_info'][0][0]['score'] += 1
            match['evaluated'] = True

        elif result == "2":
            match['match_info'][1][0]['score'] += 1
            match['evaluated'] = True

        elif result == "3":
            match['match_info'][0][0]['score'] += (1 / 2)
            match['match_info'][1][0]['score'] += (1 / 2)
            match['evaluated'] = True
        else:
            print("******* Choix invalide *******")
            tournament.match_count -= 1

        return tournament.match_count
