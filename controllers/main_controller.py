from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController


class MainController:
    """Contrôleur principal orchestrant l'application.

    Il affiche le menu principal et délègue les actions
    aux contrôleurs spécialisés (joueurs, tournois, rapports).
    """

    def __init__(self):
        """Initialise le contrôleur principal."""
        # Vue principale utilisée pour afficher le menu et les messages
        self.view = MenuView()

    def run(self):
        """Lance la boucle principale de l'application.

        Affiche le menu principal en boucle jusqu'à ce que
        l'utilisateur choisisse de quitter.
        """
        while True:
            self.view.display_main_menu()
            choice = self.view.get_input("Votre choix: ")

            if choice == '1':
                # Ouvre le sous-menu de gestion des joueurs
                PlayerController().run()
            elif choice == '2':
                # Ouvre le sous-menu de gestion des tournois
                TournamentController().run()
            elif choice == '3':
                # Ouvre le sous-menu des rapports
                ReportController().run()
            elif choice == '4':
                # Quitte l'application
                self.view.display_message("Application interrompue")
                break
            else:
                # Choix invalide : message d'erreur
                self.view.display_error("Choix invalide")
