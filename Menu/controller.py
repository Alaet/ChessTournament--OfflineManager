import os

import Database.controller as db_controller
import Database.view as db_view

from Menu.view import View

from Player.controller import PlayerController
from Player.view import PlayerView
from Player.serialize import deserialized_every_players

from Tournament.controller import TournamentController
from Tournament.serialize import serialize_tournament, serialize_tournament_players
from Tournament.view import TournamentView

from Round.controller import RoundController
from Round.serialize import serialize_round
from Round.view import RoundView

from Match.controller import MatchController


class MenuController:
    @staticmethod
    def run():
        run = True
        last_player_id = db_controller.last_player_id()
        main_view = View()
        p_view = PlayerView()
        p_controller = PlayerController(p_view, last_player_id)
        t_view = TournamentView()
        t_controller = TournamentController(t_view)
        r_view = RoundView()
        r_controller = RoundController(r_view)
        m_controller = MatchController()

        while run:
            main_menu_choice = main_view.display_main_menu()
            match main_menu_choice:
                # Player creation
                case "1":
                    new_player = p_controller.create_player()
                    if new_player is not None:
                        db_controller.insert_player(new_player)
                # Tournament creation
                case "2":
                    every_serialized_players = db_controller.get_all_players()
                    every_deserialized_players = deserialized_every_players(every_serialized_players)
                    new_tournament = t_controller.create_tournament(every_deserialized_players)
                    first_round = r_controller.generate_round(new_tournament)
                    new_tournament.rounds.append(first_round)

                    serialized_round = [serialize_round(new_tournament.rounds[0])]
                    serialized_tournament = serialize_tournament(new_tournament, serialized_round)

                    if new_tournament is not None:
                        db_controller.insert_tournament(serialized_tournament)
                # Match evaluation
                case "3":
                    deserialized_tournaments = db_controller.deserialize_all_tournaments()
                    t_r_m_choices = main_view.prompt_for_match_detail(deserialized_tournaments)
                    t_choice = t_r_m_choices[0]
                    r_choice = t_r_m_choices[1]
                    m_choice = t_r_m_choices[2]
                    if -1 in t_r_m_choices:
                        continue
                    else:
                        result = \
                            m_controller.evaluate_match(deserialized_tournaments[t_choice].rounds
                                                        [r_choice]['match_history'][m_choice],
                                                        deserialized_tournaments[t_choice])
                        # Generate next round if every match has been evaluated
                        if result == 4:
                            if not deserialized_tournaments[t_choice].round_count > \
                                   deserialized_tournaments[t_choice].turn:

                                r_controller.cloture_round(deserialized_tournaments[t_choice].rounds[r_choice])

                                deserialized_tournaments[t_choice].players_list = \
                                    serialize_tournament_players(deserialized_tournaments[t_choice].players_list)

                                next_round = r_controller.generate_round(deserialized_tournaments[t_choice])

                                serialized_round = serialize_round(next_round)
                                deserialized_tournaments[t_choice].rounds.insert(len(
                                    deserialized_tournaments[t_choice].rounds), serialized_round)
                            # Display tournament result and handle rank update
                            # (when every round is closed, and tournament over)
                            else:

                                r_controller.cloture_round(deserialized_tournaments[t_choice].rounds[r_choice])

                                t_controller.display_tournament_result(deserialized_tournaments[t_choice].rounds[
                                                                           r_choice]['match_history'])

                                p_controller.update_rank(deserialized_tournaments[t_choice].players_list)

                                deserialized_tournaments[t_choice].close = True

                                p_controller.reset_score(deserialized_tournaments[t_choice].players_list)

                                db_controller.update_players_rank(deserialized_tournaments[t_choice].players_list)

                    s_tournament = serialize_tournament(deserialized_tournaments[t_choice],
                                                        deserialized_tournaments[t_choice].rounds)
                    try:
                        s_tournament['players_list'] = serialize_tournament_players(s_tournament['players_list'])
                    except AttributeError:
                        pass

                    db_controller.update_tournament(s_tournament, t_choice)
                # Report menu
                case "4":
                    report_menu_choice = main_view.display_reports_menu()
                    every_serialized_players = db_controller.get_all_players()
                    every_deserialized_players = deserialized_every_players(every_serialized_players)
                    match report_menu_choice:
                        # Display every player in database
                        case "1":
                            main_view.display_all_players(every_deserialized_players)
                            id_player_to_update = input()
                            for deserialized_player in every_deserialized_players:
                                if id_player_to_update == str(deserialized_player.id):
                                    p_controller.update_rank([deserialized_player])
                                    db_controller.update_players_rank([deserialized_player])
                        # Display every tournament in database
                        case "2":
                            deserialized_tournaments = db_controller.deserialize_all_tournaments()
                            if len(deserialized_tournaments) == 0:
                                db_view.display_no_tournament_registered()
                                continue
                            main_view.display_all_tournaments(deserialized_tournaments)
                            t_choice_option = input()
                            if t_choice_option == "" or t_choice_option.isalpha():
                                main_view.display_invalid_choice()
                                continue
                            tournament = None
                            for x, tournament in enumerate(deserialized_tournaments):
                                if int(t_choice_option) == deserialized_tournaments.index(deserialized_tournaments[x]):
                                    tournament = deserialized_tournaments[int(t_choice_option)]
                            tournament_menu_choice = t_view.display_tournament_option_menu()

                            match tournament_menu_choice:
                                # Display every player in previously selected tournament
                                case "1":
                                    main_view.display_all_players(tournament.players_list)
                                    id_player_to_update = input()
                                    for deserialized_player in every_deserialized_players:
                                        if id_player_to_update == str(deserialized_player.id):
                                            p_controller.update_rank([deserialized_player])
                                            db_controller.update_players_rank([deserialized_player])
                                # Display every round in previously selected tournament
                                case "2":
                                    r_view.display_tournament_rounds(tournament)
                                # Display every match in previously selected tournament
                                case "3":
                                    t_view.display_tournament_matches(tournament)
                        # Return to main menu
                        case "0":
                            pass
                # Set loop checking boolean to false, then stop the execution of the application
                case "0":
                    run = False
        os.system(exit())
