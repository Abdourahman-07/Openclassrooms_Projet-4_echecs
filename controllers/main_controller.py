from views.menu_view import MenuView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from controllers.report_controller import ReportController


class MainController:
    """Contrôleur principal orchestrant l'application."""

    def __init__(self):
        """Initialise le contrôleur principal."""
        self.view = MenuView()

    def run(self):
        """Lance la boucle principale de l'application."""
        while True:
            self.view.display_main_menu()
            choice = self.view.get_input("Votre choix: ")

            if choice == '1':
                PlayerController().run()
            elif choice == '2':
                TournamentController().run()
            elif choice == '3':
                ReportController().run()
            elif choice == '4':
                self.view.display_message("Application interrompue")
                break
            else:
                self.view.display_error("Choix invalide")
