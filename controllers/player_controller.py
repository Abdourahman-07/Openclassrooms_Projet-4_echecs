from views.menu_view import MenuView
from utils.storage import Storage
from utils.validators import ask_date  # ← AJOUT


class PlayerController:
    """Contrôleur gérant les actions liées aux joueurs."""

    def __init__(self):
        """Initialise le contrôleur des joueurs."""
        self.view = MenuView()
        self.players = Storage.load_players()

    def run(self):
        """Boucle principale du menu joueurs."""
        while True:
            self.view.display_player_menu()
            choice = self.view.get_input("Votre choix: ")

            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.list_players()
            elif choice == '3':
                break
            else:
                self.view.display_error("Choix invalide")

    def add_player(self):
        """Ajoute un nouveau joueur."""
        self.view.display_message("Ajout d'un nouveau joueur")
        last_name = self.view.get_input("Nom de famille: ")
        first_name = self.view.get_input("Prénom: ")
        # birth_date = self.view.get_input("Date de naissance (YYYY-MM-DD): ")
        # ↑ ANCIEN CODE, À REMPLACER PAR :
        birth_date = ask_date(self.view, "Date de naissance (YYYY-MM-DD): ")
        national_id = self.view.get_input("Identifiant national : ")

        if national_id in self.players:
            self.view.display_error("Ce joueur existe déjà")
            return

        from models.player import Player
        player = Player(last_name, first_name, birth_date, national_id)
        self.players[national_id] = player
        Storage.save_players(self.players)
        self.view.display_success(f"Joueur {player} ajouté")

    def list_players(self):
        """Affiche la liste des joueurs par ordre alphabétique."""
        if not self.players:
            self.view.display_message("Aucun joueur enregistré")
            return

        sorted_players = sorted(
            self.players.values(),
            key=lambda player: (player.last_name, player.first_name),
        )
        self.view.display_players(sorted_players)