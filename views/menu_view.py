class MenuView:
    """Classe gérant l'affichage des menus et la saisie utilisateur."""

    def display_main_menu(self):
        """Affiche le menu principal."""
        print("\n" + "=" * 50)
        print("GESTIONNAIRE DE TOURNOIS D'ÉCHECS")
        print("=" * 50)
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Rapports")
        print("4. Quitter")
        print("=" * 50)

    def display_player_menu(self):
        """Affiche le menu de gestion des joueurs."""
        print("\n" + "-" * 50)
        print("GESTION DES JOUEURS")
        print("-" * 50)
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Retour")
        print("-" * 50)

    def display_tournament_menu(self):
        """Affiche le menu de gestion des tournois."""
        print("\n" + "-" * 50)
        print("GESTION DES TOURNOIS")
        print("-" * 50)
        print("1. Créer un tournoi")
        print("2. Inscrire des joueurs à un tournoi")
        print("3. Démarrer un nouveau tour")
        print("4. Saisir les résultats d'un tour")
        print("5. Liste des tournois")
        print("6. Retour")
        print("-" * 50)

    def display_report_menu(self):
        """Affiche le menu des rapports."""
        print("\n" + "-" * 50)
        print("RAPPORTS")
        print("-" * 50)
        print("1. Liste de tous les joueurs (ordre alphabétique)")
        print("2. Liste de tous les tournois")
        print("3. Détails d'un tournoi")
        print("4. Joueurs d'un tournoi (ordre alphabétique)")
        print("5. Tours et matchs d'un tournoi")
        print("6. Retour")
        print("-" * 50)

    def get_input(self, prompt):
        """Récupère une entrée utilisateur."""
        return input(prompt)

    def display_message(self, message):
        """Affiche un message."""
        print(f"\n{message}")

    def display_error(self, message):
        """Affiche un message d'erreur."""
        print(f"\nERREUR: {message}")

    def display_success(self, message):
        """Affiche un message de succès."""
        print(f"\n{message}")

    def display_players(self, players):
        """Affiche une liste de joueurs."""
        print("\n" + "=" * 80)
        print(f"{'ID National':<12} {'Nom':<20} {'Prénom':<20} {'Date de naissance':<15}")
        print("=" * 80)
        for player in players:
            print(f"{player.national_id:<12} {player.last_name:<20} "
                  f"{player.first_name:<20} {player.birth_date:<15}")
        print("=" * 80)

    def display_tournaments(self, tournaments):
        """Affiche une liste de tournois."""
        print("\n" + "=" * 100)
        print(f"{'Nom':<25} {'Lieu':<20} {'Début':<12} {'Fin':<12} {'Tours':<8} {'Joueurs':<8}")
        print("=" * 100)
        for tournament in tournaments:
            print(f"{tournament.name:<25} {tournament.location:<20} "
                  f"{tournament.start_date:<12} {tournament.end_date:<12} "
                  f"{tournament.current_round}/{tournament.number_of_rounds:<8} "
                  f"{len(tournament.players):<8}")
        print("=" * 100)

    def display_tournament_details(self, tournament, players_dict):
        """Affiche les détails d'un tournoi."""
        print("\n" + "=" * 80)
        print(f"Tournoi: {tournament.name}")
        print(f"Lieu: {tournament.location}")
        print(f"Date: {tournament.start_date} au {tournament.end_date}")
        print(f"Tours: {tournament.current_round}/{tournament.number_of_rounds}")
        print(f"Description: {tournament.description}")
        print("\nJoueurs inscrits:")
        for pid in tournament.players:
            if pid in players_dict:
                print(f"  - {players_dict[pid]}")
        print("=" * 80)

    def display_matches(self, matches, players_dict):
        """Affiche une liste de matchs."""
        print("\n" + "-" * 80)
        for i, match in enumerate(matches, 1):
            p1 = players_dict.get(match.player1_id, match.player1_id)
            p2 = players_dict.get(match.player2_id, match.player2_id)
            if match.score1 is not None:
                s1 = match.score1
            else:
                s1 = '-'
            if match.score2 is not None:
                s2 = match.score2
            else:
                s2 = '-'
            print(f"Match {i}: {p1} ({s1}) vs {p2} ({s2})")
        print("-" * 80)

    def display_rounds(self, tournament, players_dict):
        """Affiche tous les tours d'un tournoi."""
        print("\n" + "=" * 80)
        print(f"Tours du tournoi: {tournament.name}")
        print("=" * 80)
        for round_obj in tournament.rounds:
            print(f"\n{round_obj.name}")
            print(f"Début: {round_obj.start_datetime}")
            print(f"Fin: {round_obj.end_datetime}")
            self.display_matches(round_obj.matches, players_dict)
        print("=" * 80)
