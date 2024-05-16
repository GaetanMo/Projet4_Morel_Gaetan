
class Round:
    def __init__(self, name, start_datetime=None, end_datetime=None):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def __str__(self):
        return f"Round: {self.name}, Start Date and Time: {self.start_datetime}, End Date and Time: {self.end_datetime}"

    def add_match(self, player1, score1, player2, score2):
        self.matches.append(((player1, score1), (player2, score2)))
    