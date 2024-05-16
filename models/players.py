

class Players:
    def __init__(self, last_name, first_name, date_of_birth):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.total_points = 0 
    
    def afficher(self):
        print("Le joueur est " + self.last_name + " " + self.first_name + " et il est né le " + self.date_of_birth)


