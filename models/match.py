class Match:
    """Classe représentant un match entre deux joueurs."""

    def __init__(self, player1_id, player2_id, score1=None, score2=None):
        """Initialise un match."""
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """Convertit le match en format tuple de listes."""
        return ([self.player1_id, self.score1], [self.player2_id, self.score2])

    @classmethod
    def from_dict(cls, data):
        """Crée un match depuis le format tuple."""
        return cls(
            player1_id=data[0][0],
            player2_id=data[1][0],
            score1=data[0][1],
            score2=data[1][1]
        )

    def set_result(self, winner=None):
        """Définit le résultat du match."""
        if winner == 1:
            self.score1 = 1.0
            self.score2 = 0.0
        elif winner == 2:
            self.score1 = 0.0
            self.score2 = 1.0
        else:
            self.score1 = 0.5
            self.score2 = 0.5
