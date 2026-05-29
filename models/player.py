class Player:
    """Classe représentant un joueur d'échecs."""

    def __init__(self, last_name, first_name, birth_date, national_id):
        """Initialise un joueur."""
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id

    def to_dict(self):
        """Convertit le joueur en dictionnaire."""
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date,
            'national_id': self.national_id
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un joueur depuis un dictionnaire."""
        return cls(
            last_name=data['last_name'],
            first_name=data['first_name'],
            birth_date=data['birth_date'],
            national_id=data['national_id']
        )

    def __str__(self):
        """Représentation textuelle du joueur."""
        return f"{self.first_name} {self.last_name} ({self.national_id})"
