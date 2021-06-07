class Trainer:
    def __init__(self, name, pokemon_party, location):
        self.name = name
        self.pokemon_party = pokemon_party
        self.location = location
    
    #Function that prints out name of pokemon within your party
    def num_pokemon(self):
        for pokemon in self.pokemon_party:
            print(pokemon.name)


class Enemy:
    def __init__(self, name, quote, pokemon_party):
        self.name = name
        self.quote = quote
        self.pokemon_party = pokemon_party