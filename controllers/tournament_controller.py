from views.menu_view import MenuView
from utils.storage import Storage
from utils.pairing import PairingEngine
from models.tournament import Tournament
from models.round import Round
from utils.validators import ask_date


class TournamentController:
    """Contrôleur gérant les actions liées aux tournois."""

    def __init__(self):
        """Initialise le contrôleur des tournois."""
        self.view = MenuView()
        self.players = Storage.load_players()
        self.tournaments = Storage.load_tournaments()

    def run(self):
        """Boucle principale du menu tournois."""
        while True:
            self.view.display_tournament_menu()
            choice = self.view.get_input("Votre choix: ")

            if choice == '1':
                self.create_tournament()
            elif choice == '2':
                self.register_players()
            elif choice == '3':
                self.start_new_round()
            elif choice == '4':
                self.enter_results()
            elif choice == '5':
                self.list_tournaments()
            elif choice == '6':
                break
            else:
                self.view.display_error("Choix invalide")

    def create_tournament(self):
        """Crée un nouveau tournoi."""
        self.view.display_message("Création d'un nouveau tournoi")
        name = self.view.get_input("Nom du tournoi: ")

        if name in self.tournaments:
            self.view.display_error("Un tournoi avec ce nom existe déjà")
            return

        location = self.view.get_input("Lieu: ")
        start_date = ask_date(self.view, "Date de début (YYYY-MM-DD): ")
        end_date = ask_date(self.view, "Date de fin (YYYY-MM-DD): ")
        rounds = self.view.get_input("Nombre de tours (défaut 4): ")
        if rounds:
            rounds = int(rounds)
        else:
            rounds = 4
        description = self.view.get_input("Description (optionnel): ")

        tournament = Tournament(name, location, start_date, end_date, rounds, description=description)
        self.tournaments[name] = tournament
        Storage.save_tournament(tournament)
        self.view.display_success(f"Tournoi '{name}' créé")

    def register_players(self):
        """Inscrit des joueurs à un tournoi."""
        if not self.tournaments:
            self.view.display_error("Aucun tournoi disponible")
            return

        self.list_tournaments()
        tournament_name = self.view.get_input("Nom du tournoi: ")

        if tournament_name not in self.tournaments:
            self.view.display_error("Tournoi introuvable")
            return

        tournament = self.tournaments[tournament_name]

        if tournament.current_round > 0:
            self.view.display_error("Impossible d'ajouter des joueurs, le tournoi a déjà commencé")
            return

        while True:
            player_id = self.view.get_input("ID national du joueur (ou 'q' pour terminer): ")
            if player_id.lower() == 'q':
                break

            if player_id not in self.players:
                self.view.display_error("Joueur introuvable")
                continue

            if player_id in tournament.players:
                self.view.display_error("Joueur déjà inscrit")
                continue

            tournament.players.append(player_id)
            Storage.save_tournament(tournament)
            self.view.display_success(f"Joueur {self.players[player_id]} inscrit")

    def start_new_round(self):
        """Démarre un nouveau tour."""
        if not self.tournaments:
            self.view.display_error("Aucun tournoi disponible")
            return

        self.list_tournaments()
        tournament_name = self.view.get_input("Nom du tournoi: ")

        if tournament_name not in self.tournaments:
            self.view.display_error("Tournoi introuvable")
            return

        tournament = self.tournaments[tournament_name]

        if tournament.current_round >= tournament.number_of_rounds:
            self.view.display_error("Le tournoi est terminé")
            return

        if len(tournament.players) < 2:
            self.view.display_error("Il faut au moins 2 joueurs inscrits")
            return

        if len(tournament.players) % 2 != 0:
            self.view.display_error("Le nombre de joueurs doit être pair")
            return

        if tournament.rounds and not tournament.rounds[-1].end_datetime:
            self.view.display_error("Le tour actuel n'est pas terminé")
            return

        tournament.current_round += 1
        round_name = f"Round {tournament.current_round}"

        if tournament.current_round == 1:
            matches = PairingEngine.generate_first_round_pairs(tournament.players)
        else:
            matches = PairingEngine.generate_next_round_pairs(tournament)
        # /////////////
        new_round = Round(round_name, matches)
        new_round.start()
        tournament.rounds.append(new_round)
        Storage.save_tournament(tournament)

        self.view.display_success(f"{round_name} démarré")
        self.view.display_matches(matches, self.players)
        self.view.display_message(
            "Vous allez maintenant saisir les résultats de ce tour."
        )
        self.enter_results()

    def enter_results(self):
        """Saisit les résultats d'un tour."""
        if not self.tournaments:
            self.view.display_error("Aucun tournoi disponible")
            return

        self.list_tournaments()
        tournament_name = self.view.get_input("Nom du tournoi: ")

        if tournament_name not in self.tournaments:
            self.view.display_error("Tournoi introuvable")
            return

        tournament = self.tournaments[tournament_name]

        if not tournament.rounds:
            self.view.display_error("Aucun tour n'a été démarré")
            return

        current_round = tournament.rounds[-1]

        if current_round.end_datetime:
            self.view.display_error("Ce tour est déjà terminé")
            return

        self.view.display_message(f"Saisie des résultats pour {current_round.name}")
        self.view.display_matches(current_round.matches, self.players)

        for i, match in enumerate(current_round.matches, 1):
            p1 = self.players[match.player1_id]
            p2 = self.players[match.player2_id]
            print(f"\nMatch {i}: {p1} vs {p2}")
            result = self.view.get_input("Résultat (1=joueur1 gagne, 2=joueur2 gagne, 0=nul): ")

            if result == '1':
                match.set_result(1)
            elif result == '2':
                match.set_result(2)
            elif result == '0':
                match.set_result(0)
            else:
                self.view.display_error("Résultat invalide, match nul par défaut")
                match.set_result(0)

        current_round.end()
        Storage.save_tournament(tournament)
        self.view.display_success(f"{current_round.name} terminé")

    def list_tournaments(self):
        """Affiche la liste des tournois."""
        if not self.tournaments:
            self.view.display_message("Aucun tournoi enregistré")
            return

        sorted_tournaments = sorted(self.tournaments.values(), key=lambda tournament: tournament.name)
        self.view.display_tournaments(sorted_tournaments)
