import datetime


class Rounds:
    def __init__(self, name, start_datetime=None, end_datetime=None):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = [] #liste des matchs joués dans le tour

    def __str__(self):
        return f"Round: {self.name}, Start Date and Time: {self.start_datetime}, End Date and Time: {self.end_datetime}"
    
    def generate_pairs(self):
        # Tri des joueurs par points décroissants
        # Génération des paires
        # Mélange des paires pour éviter les matchs identiques

        
    def add_match(self, player1, score1, player2, score2):
        self.matches.append(((player1, score1), (player2, score2)))

    def start(self):
        self.start_datetime = datetime.datetime.now()

    def end(self):
        self.end_datetime = datetime.datetime.now()