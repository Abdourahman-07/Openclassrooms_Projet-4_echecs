class Player:
    """Classe représentant un joueur d'échecs.

    Un joueur est identifié de manière unique par son identifiant
    national d'échecs (national_id).
    """

    def __init__(self, last_name, first_name, birth_date, national_id):
        """Initialise un joueur.

        Args:
            last_name: Nom de famille du joueur.
            first_name: Prénom du joueur.
            birth_date: Date de naissance au format 'YYYY-MM-DD'.
            national_id: Identifiant national d'échecs (ex: 'AB12345').
        """
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id

    def to_dict(self):
        """Convertit le joueur en dictionnaire sérialisable en JSON.

        Returns:
            dict: Dictionnaire contenant les informations du joueur.
        """
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un joueur depuis un dictionnaire.

        Args:
            data: Dictionnaire contenant les clés
                  'last_name', 'first_name', 'birth_date', 'national_id'.

        Returns:
            Player: Instance de Player construite à partir du dictionnaire.
        """
        return cls(
            last_name=data["last_name"],
            first_name=data["first_name"],
            birth_date=data["birth_date"],
            national_id=data["national_id"],
        )

    def __str__(self):
        """Représentation textuelle lisible du joueur.

        Returns:
            str: Chaîne du type 'Prénom Nom (ID)'.
        """
        return f"{self.first_name} {self.last_name} ({self.national_id})"
