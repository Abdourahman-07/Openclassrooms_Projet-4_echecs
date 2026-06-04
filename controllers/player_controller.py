from views.menu_view import MenuView
from utils.storage import Storage
from utils.validators import ask_date


class PlayerController:
    """Contrôleur gérant les actions liées aux joueurs.

    Il s'occupe de l'ajout, du chargement et de l'affichage
    des joueurs enregistrés dans l'application.
    """

    def __init__(self):
        """Initialise le contrôleur des joueurs.

        Instancie la vue et charge les joueurs depuis le stockage JSON.
        """
        self.view = MenuView()
        # Dictionnaire {national_id: Player}
        self.players = Storage.load_players()

    def run(self):
        """Boucle principale du menu joueurs.

        Affiche le menu des joueurs et redirige vers les actions
        appropriées tant que l'utilisateur ne revient pas en arrière.
        """
        while True:
            self.view.display_player_menu()
            choice = self.view.get_input("Votre choix: ")

            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.list_players()
            elif choice == '3':
                # Retour au menu principal
                break
            else:
                self.view.display_error("Choix invalide")

    def add_player(self):
        """Ajoute un nouveau joueur après saisie et validation des données."""
        self.view.display_message("Ajout d'un nouveau joueur")
        last_name = self.view.get_input("Nom de famille: ")
        first_name = self.view.get_input("Prénom: ")
        # Demande une date de naissance valide au format YYYY-MM-DD
        birth_date = ask_date(self.view, "Date de naissance (YYYY-MM-DD): ")
        national_id = self.view.get_input("Identifiant national : ")

        # Vérifie qu'il n'existe pas déjà un joueur avec cet identifiant
        if national_id in self.players:
            self.view.display_error("Ce joueur existe déjà")
            return

        from models.player import Player
        player = Player(last_name, first_name, birth_date, national_id)
        # Enregistre le joueur en mémoire, indexé par son ID national
        self.players[national_id] = player
        # Sauvegarde immédiate dans le fichier JSON
        Storage.save_players(self.players)
        self.view.display_success(f"Joueur {player} ajouté")

    def list_players(self):
        """Affiche la liste des joueurs par ordre alphabétique."""
        if not self.players:
            self.view.display_message("Aucun joueur enregistré")
            return

        # Trie par nom de famille puis par prénom
        sorted_players = sorted(
            self.players.values(),
            key=lambda player: (player.last_name, player.first_name),
        )
        self.view.display_players(sorted_players)
