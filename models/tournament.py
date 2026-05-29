from .round import Round


class Tournament:
    """Classe représentant un tournoi d'échecs."""

    def __init__(self, name, location, start_date, end_date, number_of_rounds=4,
                 current_round=0, rounds=None, players=None, description=""):
        """Initialise un tournoi."""
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        if rounds is not None:
            self.rounds = rounds
        else:
            self.rounds = []
        if players is not None:
            self.players = players
        else:
            self.players = []
        self.description = description

    def to_dict(self):
        """Convertit le tournoi en dictionnaire."""
        return {
            'name': self.name,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_rounds': self.number_of_rounds,
            'current_round': self.current_round,
            'rounds': [r.to_dict() for r in self.rounds],
            'players': self.players,
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un tournoi depuis un dictionnaire."""
        rounds = [Round.from_dict(r) for r in data.get('rounds', [])]
        return cls(
            name=data['name'],
            location=data['location'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            number_of_rounds=data.get('number_of_rounds', 4),
            current_round=data.get('current_round', 0),
            rounds=rounds,
            players=data.get('players', []),
            description=data.get('description', '')
        )

    def __str__(self):
        """Représentation textuelle du tournoi."""
        return f"{self.name} - {self.location} ({self.start_date} au {self.end_date})"
