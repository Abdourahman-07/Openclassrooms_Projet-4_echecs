from utils.pairing import PairingEngine


class MenuView:
    """Classe gérant l'affichage des menus et la saisie utilisateur.

    Cette vue texte est responsable de toutes les interactions en ligne
    de commande avec l'utilisateur : affichage des menus, des listes
    (joueurs, tournois, matchs) et récupération des saisies.
    """

    def display_main_menu(self):
        """Affiche le menu principal.

        Présente les grandes sections de l'application :
        - Gestion des joueurs
        - Gestion des tournois
        - Rapports
        - Quitter l'application
        """
        print("\n" + "=" * 50)
        print("GESTIONNAIRE DE TOURNOIS D'ÉCHECS")
        print("=" * 50)
        print("1. Gestion des joueurs")
        print("2. Gestion des tournois")
        print("3. Rapports")
        print("4. Quitter")
        print("=" * 50)

    def display_player_menu(self):
        """Affiche le menu de gestion des joueurs.

        Permet de créer un joueur, d'afficher la liste des joueurs
        ou de revenir au menu principal.
        """
        print("\n" + "-" * 50)
        print("GESTION DES JOUEURS")
        print("-" * 50)
        print("1. Ajouter un joueur")
        print("2. Liste des joueurs")
        print("3. Retour")
        print("-" * 50)

    def display_tournament_menu(self):
        """Affiche le menu de gestion des tournois.

        Propose les actions principales sur les tournois :
        création, inscription des joueurs, démarrage de tour,
        saisie des résultats, consultation de la liste, retour.
        """
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
        """Affiche le menu des rapports.

        Permet de générer différents rapports sur les joueurs
        et les tournois : listes, détails, tours et matchs.
        """
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
        """Récupère une entrée utilisateur.

        Args:
            prompt: Texte affiché avant la saisie de l'utilisateur.

        Returns:
            str: Chaîne saisie par l'utilisateur (sans conversion).
        """
        return input(prompt)

    def display_message(self, message):
        """Affiche un message d'information générique.

        Args:
            message: Texte à afficher à l'utilisateur.
        """
        print(f"\n{message}")

    def display_error(self, message):
        """Affiche un message d'erreur.

        Le message est préfixé par 'ERREUR:' pour le rendre
        visuellement identifiable dans la console.

        Args:
            message: Texte décrivant l'erreur.
        """
        print(f"\nERREUR: {message}")

    def display_success(self, message):
        """Affiche un message de succès ou de confirmation.

        Args:
            message: Texte indiquant que l'action s'est bien déroulée.
        """
        print(f"\n{message}")

    def display_players(self, players):
        """Affiche une liste de joueurs dans un tableau formatté.

        Les colonnes incluent l'ID national, le nom, le prénom
        et la date de naissance.

        Args:
            players: Iterable d'objets Player à afficher.
        """
        print("\n" + "=" * 80)
        print(f"{'ID National':<12} {'Nom':<20} {'Prénom':<20} {'Date de naissance':<15}")
        print("=" * 80)
        for player in players:
            # Affiche chaque joueur sur une ligne alignée par colonnes
            print(
                f"{player.national_id:<12} {player.last_name:<20} "
                f"{player.first_name:<20} {player.birth_date:<15}"
            )
        print("=" * 80)

    def display_tournaments(self, tournaments):
        """Affiche une liste de tournois dans un tableau formaté.

        Les colonnes incluent le nom, le lieu, les dates de début/fin,
        le tour en cours / nombre total de tours, et le nombre de joueurs.

        Args:
            tournaments: Iterable d'objets Tournament à afficher.
        """
        print("\n" + "=" * 100)
        print(
            f"{'Nom':<25} {'Lieu':<20} {'Début':<12} "
            f"{'Fin':<12} {'Tours':<8} {'Joueurs':<8}"
        )
        print("=" * 100)
        for tournament in tournaments:
            # Affiche chaque tournoi sur une ligne avec les infos principales
            print(
                f"{tournament.name:<25} {tournament.location:<20} "
                f"{tournament.start_date:<12} {tournament.end_date:<12} "
                f"{tournament.current_round}/{tournament.number_of_rounds:<8} "
                f"{len(tournament.players):<8}"
            )
        print("=" * 100)

    def display_tournament_details(self, tournament, players_dict):
        """Affiche les détails d'un tournoi.

        Affiche les informations générales du tournoi (nom, lieu,
        dates, nombre de tours, description), puis la liste des
        joueurs inscrits.

        Args:
            tournament: Instance de Tournament.
            players_dict: Dictionnaire {player_id: Player} pour
                          afficher des infos lisibles sur les joueurs.
        """
        print("\n" + "=" * 80)
        print(f"Tournoi: {tournament.name}")
        print(f"Lieu: {tournament.location}")
        print(f"Date: {tournament.start_date} au {tournament.end_date}")
        print(f"Tours: {tournament.current_round}/{tournament.number_of_rounds}")
        print(f"Description: {tournament.description}")
        print("\nJoueurs inscrits:")
        for pid in tournament.players:
            if pid in players_dict:
                player = players_dict[pid]
                # Calcul du score total du joueur dans ce tournoi
                score = PairingEngine.get_player_score(tournament, pid)
                print(f"  - {player} | Points: {score}")
        print("=" * 80)

    def display_matches(self, matches, players_dict):
        """Affiche une liste de matchs avec le résultat explicite.

        Pour chaque match, affiche les deux joueurs, leurs scores
        et une phrase résumant le résultat (gagnant, nul, non saisi).

        Args:
            matches: Iterable d'objets Match.
            players_dict: Dictionnaire {player_id: Player} ou
                          {player_id: str} pour l'affichage.
        """
        print("\n" + "-" * 80)
        for i, match in enumerate(matches, 1):
            # Récupère les représentations des joueurs (objet Player ou id brut)
            p1 = players_dict.get(match.player1_id, match.player1_id)
            p2 = players_dict.get(match.player2_id, match.player2_id)

            s1 = match.score1
            s2 = match.score2

            # Texte de score (avec '-' si pas encore saisi)
            score1_txt = s1 if s1 is not None else "-"
            score2_txt = s2 if s2 is not None else "-"

            # Détermination du résultat explicite
            if s1 is None or s2 is None:
                result_txt = "résultat non saisi"
            elif s1 > s2:
                result_txt = f"{p1} gagne"
            elif s2 > s1:
                result_txt = f"{p2} gagne"
            else:
                result_txt = "match nul"

            print(
                f"Match {i}: {p1} ({score1_txt}) vs {p2} ({score2_txt})  ->  {result_txt}"
            )
        print("-" * 80)

    def display_rounds(self, tournament, players_dict):
        """Affiche tous les tours d'un tournoi avec leurs matchs.

        Pour chaque tour, affiche le nom, les dates de début/fin,
        puis délègue à `display_matches` l'affichage des matchs.

        Args:
            tournament: Instance de Tournament.
            players_dict: Dictionnaire {player_id: Player} ou
                          {player_id: str} pour l'affichage des joueurs.
        """
        print("\n" + "=" * 80)
        print(f"Tours du tournoi: {tournament.name}")
        print("=" * 80)
        for round_obj in tournament.rounds:
            print(f"\n{round_obj.name}")
            print(f"Début: {round_obj.start_datetime}")
            print(f"Fin: {round_obj.end_datetime}")
            # Affiche tous les matchs de ce tour
            self.display_matches(round_obj.matches, players_dict)
        print("=" * 80)
