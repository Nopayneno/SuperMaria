class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.score = 0

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f'Player: {self.name}, Health: {self.health}, Score: {self.score}'