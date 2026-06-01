from views.menu_view import MenuView
from utils.storage import Storage


class PlayerController:
    """Contrôleur gérant les actions liées aux joueurs."""

    def __init__(self):
        """Initialise le contrôleur des joueurs."""
        self.view = MenuView()
        # Charge tous les joueurs depuis le fichier JSON au démarrage
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
                # Sortie de la boucle pour retourner au menu principal
                break
            else:
                self.view.display_error("Choix invalide")

    def add_player(self):
        """Ajoute un nouveau joueur."""
        self.view.display_message("Ajout d'un nouveau joueur")
        last_name = self.view.get_input("Nom de famille: ")
        first_name = self.view.get_input("Prénom: ")
        birth_date = self.view.get_input("Date de naissance (YYYY-MM-DD): ")
        national_id = self.view.get_input("Identifiant national : ")

        # Vérifie que le joueur n'existe pas déjà
        if national_id in self.players:
            self.view.display_error("Ce joueur existe déjà")
            return

        from models.player import Player
        player = Player(last_name, first_name, birth_date, national_id)
        # Ajoute le joueur au dictionnaire avec son ID comme clé
        self.players[national_id] = player
        # Sauvegarde immédiatement dans le fichier JSON
        Storage.save_players(self.players)
        self.view.display_success(f"Joueur {player} ajouté")

    def list_players(self):
        """Affiche la liste des joueurs par ordre alphabétique."""
        if not self.players:
            self.view.display_message("Aucun joueur enregistré")
            return

        # Trie par nom de famille, puis par prénom
        sorted_players = sorted(
            self.players.values(),
            key=lambda player: (player.last_name, player.first_name)
        )
        self.view.display_players(sorted_players)