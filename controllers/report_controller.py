from views.menu_view import MenuView
from utils.storage import Storage


class ReportController:
    """Contrôleur gérant les rapports.

    Il permet d'afficher différentes vues en lecture seule
    sur les joueurs et les tournois (listes, détails, historiques).
    """

    def __init__(self):
        """Initialise le contrôleur des rapports.

        Charge en mémoire les joueurs et tournois existants
        pour générer les rapports.
        """
        self.view = MenuView()
        # Dictionnaire {national_id: Player}
        self.players = Storage.load_players()
        # Dictionnaire {tournament_name: Tournament}
        self.tournaments = Storage.load_tournaments()

    def run(self):
        """Boucle principale du menu rapports.

        Affiche le menu des rapports et exécute l'action
        choisie par l'utilisateur jusqu'au retour au menu principal.
        """
        while True:
            self.view.display_report_menu()
            choice = self.view.get_input("Votre choix: ")

            if choice == '1':
                self.all_players_alphabetical()
            elif choice == '2':
                self.all_tournaments()
            elif choice == '3':
                self.tournament_details()
            elif choice == '4':
                self.tournament_players()
            elif choice == '5':
                self.tournament_rounds()
            elif choice == '6':
                # Retour au menu principal
                break
            else:
                self.view.display_error("Choix invalide")

    def all_players_alphabetical(self):
        """Affiche tous les joueurs par ordre alphabétique global."""
        if not self.players:
            self.view.display_message("Aucun joueur enregistré")
            return

        # Tri par nom de famille puis par prénom
        sorted_players = sorted(
            self.players.values(),
            key=lambda player: (player.last_name, player.first_name),
        )
        self.view.display_players(sorted_players)

    def all_tournaments(self):
        """Affiche la liste de tous les tournois enregistrés."""
        if not self.tournaments:
            self.view.display_message("Aucun tournoi enregistré")
            return

        # Tri par nom de tournoi
        sorted_tournaments = sorted(
            self.tournaments.values(),
            key=lambda tournament: tournament.name,
        )
        self.view.display_tournaments(sorted_tournaments)

    def tournament_details(self):
        """Affiche les détails d'un tournoi choisi par l'utilisateur."""
        if not self.tournaments:
            self.view.display_error("Aucun tournoi disponible")
            return

        # Affiche d'abord la liste des tournois pour aider au choix
        self.all_tournaments()
        tournament_name = self.view.get_input("Nom du tournoi: ")

        if tournament_name not in self.tournaments:
            self.view.display_error("Tournoi non enregistré")
            return

        tournament = self.tournaments[tournament_name]
        self.view.display_tournament_details(tournament, self.players)

    def tournament_players(self):
        """Affiche les joueurs d'un tournoi par ordre alphabétique."""
        if not self.tournaments:
            self.view.display_error("Aucun tournoi prévu")
            return

        # Affiche la liste des tournois pour choisir
        self.all_tournaments()
        tournament_name = self.view.get_input("Nom du tournoi: ")

        if tournament_name not in self.tournaments:
            self.view.display_error("Tournoi introuvable")
            return

        tournament = self.tournaments[tournament_name]
        # Récupère les objets Player correspondant aux IDs enregistrés
        tournament_players = [
            self.players[player_id]
            for player_id in tournament.players
            if player_id in self.players
        ]
        # Tri par nom de famille puis par prénom
        sorted_players = sorted(
            tournament_players,
            key=lambda player: (player.last_name, player.first_name),
        )

        self.view.display_message(f"Joueurs du tournoi '{tournament.name}':")
        self.view.display_players(sorted_players)

    def tournament_rounds(self):
        """Affiche tous les tours et matchs d'un tournoi."""
        if not self.tournaments:
            self.view.display_error("Aucun tournoi disponible")
            return

        # Affiche d'abord la liste des tournois pour aider au choix
        self.all_tournaments()
        tournament_name = self.view.get_input("Nom du tournoi: ")

        if tournament_name not in self.tournaments:
            self.view.display_error("Tournoi introuvable")
            return

        tournament = self.tournaments[tournament_name]
        if not tournament.rounds:
            self.view.display_message("Aucun tour n'a été joué")
            return

        # Affiche chaque round et ses matchs (avec résultats)
        self.view.display_rounds(tournament, self.players)
