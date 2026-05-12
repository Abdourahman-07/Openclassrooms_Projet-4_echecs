class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        description="",
        number_of_rounds=4,
        current_round=0,
        rounds=None,
        players=None,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.current_round = current_round
        self.rounds = rounds or []
        self.players = players or []

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, new_round):
        self.rounds.append(new_round)
        self.current_round = len(self.rounds)

