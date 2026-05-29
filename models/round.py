from datetime import datetime
from .match import Match


class Round:
    """Classe représentant un tour d'un tournoi."""

    def __init__(self, name, matches=None, start_datetime=None, end_datetime=None):
        """Initialise un tour."""
        self.name = name
        if matches is not None:
            self.matches = matches
        else:
            self.matches = []
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def start(self):
        """Démarre le tour en enregistrant la date/heure."""
        self.start_datetime = datetime.now().isoformat()

    def end(self):
        """Termine le tour en enregistrant la date/heure."""
        self.end_datetime = datetime.now().isoformat()

    def to_dict(self):
        """Convertit le tour en dictionnaire."""
        return {
            'name': self.name,
            'matches': [m.to_dict() for m in self.matches],
            'start_datetime': self.start_datetime,
            'end_datetime': self.end_datetime
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un tour depuis un dictionnaire."""
        matches = [Match.from_dict(m) for m in data.get('matches', [])]
        return cls(
            name=data['name'],
            matches=matches,
            start_datetime=data.get('start_datetime'),
            end_datetime=data.get('end_datetime')
        )

    def __str__(self):
        """Représentation textuelle du tour."""
        return f"{self.name} - {len(self.matches)} matchs"
