import random
from models.match import Match


class PairingEngine:
    """Moteur de génération des appariements pour les tournois.

    Implémente une logique de type système suisse simplifié :
    - 1er tour : appariement aléatoire.
    - Tours suivants : appariement par groupes de score, en évitant
      si possible les re-rencontres.
    """

    @staticmethod
    def generate_first_round_pairs(player_ids):
        """Génère les paires du premier tour par mélange aléatoire.

        Args:
            player_ids: Liste des identifiants des joueurs.

        Returns:
            list[Match]: Liste de matchs (player1_id, player2_id).

        Note:
            Si le nombre de joueurs est impair, le dernier joueur
            est ignoré pour le moment (pas de bye géré ici).
        """
        shuffled = player_ids.copy()
        random.shuffle(shuffled)
        matches = []
        for i in range(0, len(shuffled), 2):
            if i + 1 < len(shuffled):
                matches.append(Match(shuffled[i], shuffled[i + 1]))
        return matches

    @staticmethod
    def get_player_score(tournament, player_id):
        """Calcule le score total d'un joueur dans le tournoi.

        Args:
            tournament: Instance de Tournament.
            player_id: Identifiant du joueur.

        Returns:
            float: Score cumulé du joueur (somme des scores de chaque match).
        """
        score = 0.0
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                if match.player1_id == player_id and match.score1 is not None:
                    score += match.score1
                elif match.player2_id == player_id and match.score2 is not None:
                    score += match.score2
        return score

    @staticmethod
    def get_player_opponents(tournament, player_id):
        """Récupère la liste des adversaires déjà affrontés.

        Args:
            tournament: Instance de Tournament.
            player_id: Identifiant du joueur.

        Returns:
            set: Ensemble des IDs des adversaires déjà rencontrés.
        """
        opponents = set()
        for round_obj in tournament.rounds:
            for match in round_obj.matches:
                if match.player1_id == player_id:
                    opponents.add(match.player2_id)
                elif match.player2_id == player_id:
                    opponents.add(match.player1_id)
        return opponents

    @classmethod
    def generate_next_round_pairs(cls, tournament):
        """Génère les paires pour le tour suivant sur la base des scores.

        Logique:
        - Calcule le score de chaque joueur.
        - Trie les joueurs par score décroissant.
        - Parcourt la liste en essayant de leur trouver un adversaire
          qu'ils n'ont pas encore rencontré.
        - Si ce n'est pas possible, accepte une re-rencontre en dernier recours.

        Args:
            tournament: Instance de Tournament, avec les rounds déjà joués
                        et la liste `players` remplie.

        Returns:
            list[Match]: Liste de matchs pour le prochain tour.
        """
        players_scores = []
        for player_id in tournament.players:
            score = cls.get_player_score(tournament, player_id)
            players_scores.append((player_id, score))

        # Tri par score décroissant, puis aléatoire pour départager les ex aequo
        players_scores.sort(key=lambda x: (-x[1], random.random()))

        available = [p[0] for p in players_scores]
        matches = []

        while len(available) >= 2:
            player1 = available.pop(0)
            opponents = cls.get_player_opponents(tournament, player1)

            paired = False
            # Cherche un joueur avec le même score (ou proche) qui n'a pas
            # encore été rencontré. Ici, on se contente de respecter l'ordre
            # dans `available`, déjà trié par score.
            for i, player2 in enumerate(available):
                if player2 not in opponents:
                    available.pop(i)
                    matches.append(Match(player1, player2))
                    paired = True
                    break

            # Si aucun partenaire "nouveau" n'a été trouvé,
            # on accepte une re-rencontre.
            if not paired and available:
                player2 = available.pop(0)
                matches.append(Match(player1, player2))

        return matches
