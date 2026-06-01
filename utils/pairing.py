import random
from models.match import Match


class PairingEngine:
    """Moteur de génération des appariements pour les tournois."""

    @staticmethod
    def generate_first_round_pairs(player_ids):
        """Génère les paires du premier tour (mélange aléatoire)."""
        shuffled = player_ids.copy()
        random.shuffle(shuffled)
        matches = []
        for i in range(0, len(shuffled), 2):
            if i + 1 < len(shuffled):
                matches.append(Match(shuffled[i], shuffled[i + 1]))
        return matches

    @staticmethod
    def get_player_score(tournament, player_id):
        """Calcule le score total d'un joueur dans le tournoi."""
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
        """Récupère la liste des adversaires déjà affrontés."""
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
        """Génère les paires pour le tour suivant basé sur les scores."""
        players_scores = []
        for player_id in tournament.players:
            score = cls.get_player_score(tournament, player_id)
            players_scores.append((player_id, score))

        players_scores.sort(key=lambda x: (-x[1], random.random()))

        available = [p[0] for p in players_scores]
        matches = []

        while len(available) >= 2:
            player1 = available.pop(0)
            opponents = cls.get_player_opponents(tournament, player1)

            paired = False
            for i, player2 in enumerate(available):
                if player2 not in opponents:
                    available.pop(i)
                    matches.append(Match(player1, player2))
                    paired = True
                    break

            if not paired and available:
                player2 = available.pop(0)
                matches.append(Match(player1, player2))

        return matches
