from .round import Round


class Tournament:
    """Classe représentant un tournoi d'échecs.

    Un tournoi contient un nom, un lieu, des dates de début et de fin,
    un nombre de tours, la liste des tours joués, la liste des joueurs
    inscrits et une description optionnelle.
    """

    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        number_of_rounds=4,
        current_round=0,
        rounds=None,
        players=None,
        description="",
    ):
        """Initialise un tournoi.

        Args:
            name: Nom du tournoi.
            location: Lieu où se déroule le tournoi.
            start_date: Date de début au format 'YYYY-MM-DD'.
            end_date: Date de fin au format 'YYYY-MM-DD'.
            number_of_rounds: Nombre total de tours prévus (par défaut 4).
            current_round: Numéro du tour actuel (0 tant que le tournoi n'a pas commencé).
            rounds: Liste d'instances de Round (peut être None au départ).
            players: Liste des identifiants nationaux des joueurs inscrits.
            description: Texte libre pour les remarques du directeur de tournoi.
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round

        # S'assure que rounds est toujours une liste
        if rounds is not None:
            self.rounds = rounds
        else:
            self.rounds = []

        # S'assure que players est toujours une liste
        if players is not None:
            self.players = players
        else:
            self.players = []

        self.description = description

    def to_dict(self):
        """Convertit le tournoi en dictionnaire sérialisable en JSON.

        Returns:
            dict: Représentation du tournoi contenant ses méta-données,
                  la liste des tours (convertis en dict) et la liste des joueurs.
        """
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_of_rounds": self.number_of_rounds,
            "current_round": self.current_round,
            "rounds": [r.to_dict() for r in self.rounds],
            "players": self.players,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un tournoi depuis un dictionnaire.

        Args:
            data: Dictionnaire contenant les clés du tournoi
                  (généralement chargé depuis un fichier JSON).

        Returns:
            Tournament: Instance de Tournament reconstruite à partir des données.
        """
        rounds = [Round.from_dict(r) for r in data.get("rounds", [])]
        return cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            number_of_rounds=data.get("number_of_rounds", 4),
            current_round=data.get("current_round", 0),
            rounds=rounds,
            players=data.get("players", []),
            description=data.get("description", ""),
        )

    def __str__(self):
        """Représentation textuelle lisible du tournoi.

        Returns:
            str: Chaîne du type 'Nom - Lieu (YYYY-MM-DD au YYYY-MM-DD)'.
        """
        return f"{self.name} - {self.location} ({self.start_date} au {self.end_date})"
