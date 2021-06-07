class Pokemon:
    def __init__(self, name, health, max_health, attacks):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attacks = attacks

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
