class Player:
    def __init__(self, last_name, first_name, birth_date, national_id, points=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.points = points

    def add_points(self, score):
        self.points += score

    def to_dictionnary(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "points": self.points,
        }

    def from_dictionnary(cls, data):
        return cls(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["national_id"],
            data.get("points", 0),
        )
