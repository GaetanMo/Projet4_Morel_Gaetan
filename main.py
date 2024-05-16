from controllers.players_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.round_controller import RoundController
from views.console import ConsoleView

def main():
    player_controller = PlayerController()
    tournament_controller = TournamentController()
    round_controller = RoundController()
    console_view = ConsoleView()

    while True:
        console_view.main_menu()
        choice = input("\nChoisissez une option: ")

        if choice == "1":
            players = player_controller.get_players()
            console_view.display_players(players)
        elif choice == "2":
            tournaments = tournament_controller.get_tournaments()
            console_view.display_tournaments(tournaments)
        elif choice == "3":
            tournament_idx = int(input("Entrez l'index du tournoi: ")) - 1
            tournament = tournament_controller.get_tournament_by_index(tournament_idx)
            console_view.display_tournament_details(tournament)
        elif choice == "4":
            console_view.display_reports()
            # Ajoutez la logique pour afficher les rapports ici
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()