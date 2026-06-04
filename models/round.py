from datetime import datetime
from .match import Match


class Round:
    """Classe représentant un tour d'un tournoi.

    Un tour contient un nom, une liste de matchs, ainsi que les
    dates/heures de début et de fin.
    """

    def __init__(self, name, matches=None, start_datetime=None, end_datetime=None):
        """Initialise un tour.

        Args:
            name: Nom du tour (ex: 'Round 1').
            matches: Liste d'instances de Match (peut être None au départ).
            start_datetime: Date/heure de début au format ISO 8601 (str ou None).
            end_datetime: Date/heure de fin au format ISO 8601 (str ou None).
        """
        self.name = name
        # S'assure que matches est toujours une liste
        if matches is not None:
            self.matches = matches
        else:
            self.matches = []
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def start(self):
        """Démarre le tour en enregistrant la date/heure actuelle.

        La date/heure est stockée au format ISO 8601 (via datetime.now().isoformat()).
        """
        self.start_datetime = datetime.now().isoformat()

    def end(self):
        """Termine le tour en enregistrant la date/heure actuelle."""
        self.end_datetime = datetime.now().isoformat()

    def to_dict(self):
        """Convertit le tour en dictionnaire sérialisable en JSON.

        Returns:
            dict: Représentation du tour contenant son nom, la liste
                  des matchs convertis en dict/tuples, et les dates
                  de début/fin.
        """
        return {
            "name": self.name,
            "matches": [m.to_dict() for m in self.matches],
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime,
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un tour depuis un dictionnaire.

        Args:
            data: Dictionnaire contenant au minimum 'name' et optionnellement
                  'matches', 'start_datetime' et 'end_datetime'.

        Returns:
            Round: Instance de Round reconstruite à partir des données.
        """
        matches = [Match.from_dict(m) for m in data.get("matches", [])]
        return cls(
            name=data["name"],
            matches=matches,
            start_datetime=data.get("start_datetime"),
            end_datetime=data.get("end_datetime"),
        )

    def __str__(self):
        """Représentation textuelle du tour.

        Returns:
            str: Chaîne du type 'Round 1 - 4 matchs'.
        """
        return f"{self.name} - {len(self.matches)} matchs"
