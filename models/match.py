class Match:
    """Classe représentant un match entre deux joueurs.

    Les scores sont stockés côté joueur 1 et côté joueur 2,
    avec les valeurs possibles : 1.0, 0.5 ou 0.0.
    """

    def __init__(self, player1_id, player2_id, score1=None, score2=None):
        """Initialise un match.

        Args:
            player1_id: Identifiant national du premier joueur.
            player2_id: Identifiant national du second joueur.
            score1: Score du premier joueur (float ou None).
            score2: Score du second joueur (float ou None).
        """
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """Convertit le match en format tuple de listes.

        Retourne un objet compatible JSON, sous la forme :
        ([player1_id, score1], [player2_id, score2])
        """
        return [  # JSON stockera ça comme une liste de deux listes
            [self.player1_id, self.score1],
            [self.player2_id, self.score2],
        ]

    @classmethod
    def from_dict(cls, data):
        """Crée un match depuis le format tuple/list de listes.

        Args:
            data: Structure de la forme [[player1_id, score1], [player2_id, score2]]

        Returns:
            Une instance de Match initialisée avec ces valeurs.
        """
        return cls(
            player1_id=data[0][0],
            player2_id=data[1][0],
            score1=data[0][1],
            score2=data[1][1],
        )

    def set_result(self, winner=None):
        """Définit le résultat du match en fonction du vainqueur.

        Args:
            winner:
                1  -> joueur 1 gagne (1.0 / 0.0)
                2  -> joueur 2 gagne (0.0 / 1.0)
                0  -> match nul (0.5 / 0.5)
                None ou autre valeur -> match nul (0.5 / 0.5)
        """
        if winner == 1:
            self.score1 = 1.0
            self.score2 = 0.0
        elif winner == 2:
            self.score1 = 0.0
            self.score2 = 1.0
        else:
            self.score1 = 0.5
            self.score2 = 0.5
