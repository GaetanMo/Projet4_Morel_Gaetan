class ConsoleView:
    def __init__(self):
        pass

    def main_menu(self):
        print("\n--- MENU PRINCIPAL ---")
        print("1. Afficher la liste des joueurs")
        print("2. Afficher la liste des tournois")
        print("3. Afficher les détails d'un tournoi")
        print("4. Afficher les rapports")
        print("5. Quitter")

    def display_players(self, players):
        print("\n--- LISTE DES JOUEURS ---")
        for idx, player in enumerate(players, start=1):
            print(f"{idx}. {player}")

    def display_tournaments(self, tournaments):
        print("\n--- LISTE DES TOURNOIS ---")
        for idx, tournament in enumerate(tournaments, start=1):
            print(f"{idx}. {tournament}")

    def display_tournament_details(self, tournament):
        print("\n--- DÉTAILS DU TOURNOI ---")
        print(tournament)

    def display_reports(self):
        print("\n--- RAPPORTS ---")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Nom et dates d'un tournoi donné")
        print("4. Liste des joueurs du tournoi par ordre alphabétique")
        print("5. Liste de tous les tours du tournoi et de tous les matchs du tour")
        print("Retour au menu principal")