

class Tournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, current_round=1, rounds=None, players=None, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = rounds if rounds else []
        self.players = players if players else []
        self.description = description
    
    def __str__(self):
        return f"Tournament {self.name} - Location: {self.location}, Dates: {self.start_date} to {self.end_date}"

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round_matches):
        self.rounds.append(round_matches)

    def record_result(self, match, result):
        pass

    