import tinydb.database

from Menu.view import View
from Player.controller import PlayerController
from Player.serialize import serialize_player
from Player.view import PlayerView
from Tournament.controller import TournamentController
from Tournament.serialize import serialize_tournament, deserialized_tournament_players, \
    serialize_tournament_players,  deserialize_tournament
from Tournament.view import TournamentView
from Round.controller import RoundController
from Round.serialize import serialize_round
from Round.view import RoundView

from tinydb import TinyDB, Query

db = TinyDB('db.json')
players_table = db.table('players')
tournament_table = db.table('tournaments')


class MenuController:

    @staticmethod
    def run():
        run = True
        all_tournaments = []

        main_view = View()
        player_view = PlayerView()
        player_controller = PlayerController(player_view)
        tournament_view = TournamentView()
        tournament_controller = TournamentController(tournament_view)
        round_view = RoundView()
        round_controller = RoundController(round_view)
        while run:
            main_menu_choice = main_view.display_main_menu()
            match main_menu_choice:
                case "1":
                    new_player = player_controller.create_player()
                    if new_player is not None:
                        players_table.insert(new_player)

                case "2":
                    serialized_players = players_table.all()
                    deserialized_new_tournament_players = deserialized_tournament_players(serialized_players)
                    new_tournament = tournament_controller.create_tournament(deserialized_new_tournament_players)
                    first_round = round_controller.generate_round(new_tournament)
                    new_tournament.rounds.append(first_round)

                    serialized_round = [serialize_round(new_tournament.rounds[0])]
                    serialized_tournament = serialize_tournament(new_tournament, serialized_round)

                    if new_tournament is not None:
                        tournament_table.insert(serialized_tournament)

                case "3":
                    serialized_tournaments = tournament_table.all()
                    deserialized_tournaments = []

                    for t_serial in serialized_tournaments:

                        d_tourn_player = deserialized_tournament_players(t_serial['players_list'])

                        d_tourn = deserialize_tournament(t_serial)

                        d_tourn.players_list = d_tourn_player

                        deserialized_tournaments.append(d_tourn)
                    detail_choices = main_view.prompt_for_match_detail(deserialized_tournaments)
                    if -1 in detail_choices:
                        continue
                    else:
                        result = tournament_controller.evaluate_match(deserialized_tournaments[detail_choices[0]].
                                                                      rounds[detail_choices[1]]
                                                                      ['match_history'][detail_choices[2]],
                                                                      deserialized_tournaments[detail_choices[0]])

                        if result == 4:
                            if not deserialized_tournaments[detail_choices[0]].round_count > deserialized_tournaments[
                                   detail_choices[0]].turn:

                                tournament_controller.cloture_round(deserialized_tournaments[detail_choices[0]].
                                                                    rounds[detail_choices[1]])

                                deserialized_tournaments[detail_choices[0]].players_list = \
                                    serialize_tournament_players(deserialized_tournaments[detail_choices[0]].
                                                                 players_list)

                                next_round = round_controller.\
                                    generate_round(deserialized_tournaments[detail_choices[0]])

                                serialized_round = serialize_round(next_round)
                                deserialized_tournaments[detail_choices[0]].rounds.insert(len(
                                    deserialized_tournaments[detail_choices[0]].rounds), serialized_round)

                            else:
                                player_controller.update_rank(deserialized_tournaments[detail_choices[0]].players_list)
                                for x, player in enumerate(deserialized_tournaments[detail_choices[0]].players_list):
                                    User = Query()
                                    db_player_update = serialize_player(player)
                                    players_table.upsert(db_player_update, User.name == str(player.name))
                                deserialized_tournaments[detail_choices[0]].close = True
                                tournament_controller.reset_score(
                                    deserialized_tournaments[detail_choices[0]].players_list)

                    s_tournament = serialize_tournament(deserialized_tournaments[detail_choices[0]],
                                                        deserialized_tournaments[detail_choices[0]].rounds)
                    try:
                        s_tournament['players_list'] = serialize_tournament_players(s_tournament['players_list'])
                    except AttributeError:
                        pass

                    t_doc = tournament_table.get(doc_id=detail_choices[0]+1)

                    tournament_table.upsert(tinydb.database.Document(s_tournament, doc_id=t_doc.doc_id))

                case "4":
                    report_menu_choice = main_view.display_reports_menu()
                    match report_menu_choice:
                        case "1":
                            serialized_players = players_table.all()
                            deserialized_new_tournament_players = deserialized_tournament_players(
                                serialized_players)
                            main_view.display_all_players(deserialized_new_tournament_players)
                        case "2":
                            serialized_tournaments = tournament_table.all()
                            deserialized_tournaments = []

                            for t_serial in serialized_tournaments:
                                d_tourn_player = deserialized_tournament_players(t_serial['players_list'])

                                d_tourn = deserialize_tournament(t_serial)

                                d_tourn.players_list = d_tourn_player

                                deserialized_tournaments.append(d_tourn)
                            main_view.display_all_tournaments(deserialized_tournaments)
                            t_choice = input()
                            if t_choice == "" or t_choice.isalpha():
                                main_view.display_invalid_choice()
                                continue
                            for x, t in enumerate(deserialized_tournaments):
                                if int(t_choice) == deserialized_tournaments.index(deserialized_tournaments[x]):
                                    tournament = deserialized_tournaments[int(t_choice)]
                            tournament_menu_choice = tournament_view.display_tournament_option_menu()
                            match tournament_menu_choice:
                                case "1":
                                    main_view.display_all_players(tournament.players_list)
                                case "2":
                                    tournament_view.display_tournament_rounds(tournament)
                                case "3":
                                    tournament_view.display_tournament_matches(tournament)
                case "0":
                    run = False
