import Database.controller

from Menu.view import View
from Player.controller import PlayerController
from Player.view import PlayerView
from Tournament.controller import TournamentController
from Tournament.serialize import serialize_tournament, deserialized_every_players, serialize_tournament_players
from Tournament.view import TournamentView
from Round.controller import RoundController
from Round.serialize import serialize_round
from Round.view import RoundView


class MenuController:

    @staticmethod
    def run():
        run = True

        main_view = View()
        player_view = PlayerView()
        player_controller = PlayerController(player_view)
        tournament_view = TournamentView()
        t_controller = TournamentController(tournament_view)
        round_view = RoundView()
        round_controller = RoundController(round_view)
        while run:
            main_menu_choice = main_view.display_main_menu()
            match main_menu_choice:
                case "1":
                    new_player = player_controller.create_player()
                    if new_player is not None:
                        Database.controller.insert_player(new_player)

                case "2":
                    every_serialized_players = Database.controller.get_all_players()
                    every_deserialized_players = deserialized_every_players(every_serialized_players)
                    new_tournament = t_controller.create_tournament(every_deserialized_players)
                    first_round = round_controller.generate_round(new_tournament)
                    new_tournament.rounds.append(first_round)

                    serialized_round = [serialize_round(new_tournament.rounds[0])]
                    serialized_tournament = serialize_tournament(new_tournament, serialized_round)

                    if new_tournament is not None:
                        Database.controller.insert_player(serialized_tournament)

                case "3":
                    every_serialized_tournaments = Database.controller.get_all_tournaments()
                    deserialized_tournaments = Database.controller.deserialize_all_tournaments(
                        every_serialized_tournaments)
                    t_r_m_choices = main_view.prompt_for_match_detail(deserialized_tournaments)
                    if -1 in t_r_m_choices:
                        continue
                    else:
                        result = t_controller.evaluate_match(deserialized_tournaments[t_r_m_choices[0]].rounds[
                                                                 t_r_m_choices[1]]['match_history'][t_r_m_choices[2]]
                                                             , deserialized_tournaments[t_r_m_choices[0]])

                        if result == 4:
                            if not deserialized_tournaments[t_r_m_choices[0]].round_count > deserialized_tournaments[
                                   t_r_m_choices[0]].turn:

                                t_controller.cloture_round(deserialized_tournaments[t_r_m_choices[0]].
                                                           rounds[t_r_m_choices[1]])

                                deserialized_tournaments[t_r_m_choices[0]].players_list = \
                                    serialize_tournament_players(deserialized_tournaments[t_r_m_choices[
                                        0]].players_list)

                                next_round = round_controller.generate_round(deserialized_tournaments[
                                                                                  t_r_m_choices[0]])

                                serialized_round = serialize_round(next_round)
                                deserialized_tournaments[t_r_m_choices[0]].rounds.insert(len(
                                    deserialized_tournaments[t_r_m_choices[0]].rounds), serialized_round)

                            else:
                                player_controller.update_rank(deserialized_tournaments[t_r_m_choices[0]].players_list)

                                Database.controller.\
                                    update_players_rank(deserialized_tournaments[t_r_m_choices[0]].players_list)

                                deserialized_tournaments[t_r_m_choices[0]].close = True

                                t_controller.reset_score(deserialized_tournaments[t_r_m_choices[0]].players_list)

                    s_tournament = serialize_tournament(deserialized_tournaments[t_r_m_choices[0]],
                                                        deserialized_tournaments[t_r_m_choices[0]].rounds)
                    try:
                        s_tournament['players_list'] = serialize_tournament_players(s_tournament['players_list'])
                    except AttributeError:
                        pass

                    Database.controller.update_tournament(s_tournament, t_r_m_choices[0])

                case "4":
                    report_menu_choice = main_view.display_reports_menu()
                    match report_menu_choice:
                        case "1":
                            every_serialized_players = Database.controller.get_all_players()
                            every_deserialized_players = deserialized_every_players(
                                every_serialized_players)
                            main_view.display_all_players(every_deserialized_players)
                        case "2":
                            every_serialized_tournaments = Database.controller.get_all_tournaments()
                            deserialized_tournaments = Database.controller.deserialize_all_tournaments(
                                every_serialized_tournaments)

                            main_view.display_all_tournaments(deserialized_tournaments)
                            t_choice = input()
                            if t_choice == "" or t_choice.isalpha():
                                main_view.display_invalid_choice()
                                continue
                            tournament = None
                            for x, tournament in enumerate(deserialized_tournaments):
                                if int(t_choice) == deserialized_tournaments.index(deserialized_tournaments[x]):
                                    tournament = deserialized_tournaments[int(t_choice)]
                            tournament_menu_choice = tournament_view.display_tournament_option_menu()

                            match tournament_menu_choice:
                                case "1":
                                    main_view.display_all_players(tournament.players_list)
                                case "2":
                                    round_view.display_tournament_rounds(tournament)
                                case "3":
                                    tournament_view.display_tournament_matches(tournament)
                case "0":
                    run = False
