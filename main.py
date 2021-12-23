from Menu.view import View
from Player.controller import PlayerController
from Player.view import PlayerView
from Tournament.controller import TournamentController
from Tournament.view import TournamentView
from Round.controller import RoundController
from Round.view import RoundView
from tinydb import TinyDB, Query

db = TinyDB('db.json')
players_table = db.table('players')
tournament_table = db.table('tournaments')
serialized_players = players_table.all()


def main():

    run = True
    all_players = []
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
                    players_table.insert(new_player[1])
                    all_players.append(new_player[0])
            case "2":
                new_tournament = tournament_controller.create_tournament(serialized_players)
                if new_tournament is not None:
                    tournament_table.insert(new_tournament)
                    all_tournaments.append(new_tournament)
                deserialized_tournament = tournament_controller.deserialize_tournament(new_tournament)
                first_round = round_controller.generate_round(deserialized_tournament)
                tournament_table.update({'rounds': first_round})
                # SERIALIZE MATCH ROUND voir deplacer generation match du model vers round controller into match
                # controller ?
                # new_tournament.rounds.append(first_round)

            case "3":
                detail_choices = main_view.prompt_for_match_detail(all_tournaments)
                if -1 in detail_choices:
                    pass
                else:
                    result = tournament_controller.evaluate_match(all_tournaments[detail_choices[0]].
                                                                  rounds[detail_choices[1]].
                                                                  match_history[detail_choices[2]],
                                                                  all_tournaments[detail_choices[0]])

                    if result == 4:
                        if not all_tournaments[detail_choices[0]].round_count > all_tournaments[detail_choices[0]].\
                                turn:

                            tournament_controller.cloture_round(all_tournaments[detail_choices[0]].
                                                                rounds[detail_choices[1]])

                            next_round = round_controller.generate_round(all_tournaments[detail_choices[0]])
                            all_tournaments[detail_choices[0]].rounds.append(next_round)
                        else:
                            player_controller.update_rank(all_tournaments[detail_choices[0]].players_list)
                            for x, player in enumerate(all_tournaments[detail_choices[0]].players_list):
                                User = Query()
                                db_player_update = player_controller.serialize_player(player)
                                players_table.upsert(db_player_update, User.name == str(player.name))
                            all_tournaments[detail_choices[0]].close = True
                            tournament_controller.reset_score(all_tournaments[detail_choices[0]].players_list)

            case "4":
                report_menu_choice = main_view.display_reports_menu()
                match report_menu_choice:
                    case "1":
                        deserialized_players = tournament_controller.deserialized_tournament_players(
                            serialized_players)
                        main_view.display_all_players(deserialized_players)
                    case "2":
                        main_view.display_all_tournaments(all_tournaments)
                        t_choice = input()
                        for x, t in enumerate(all_tournaments):
                            if int(t_choice) == all_tournaments.index(all_tournaments[x]):
                                tournament = all_tournaments[int(t_choice)]
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


if __name__ == '__main__':
    main()
