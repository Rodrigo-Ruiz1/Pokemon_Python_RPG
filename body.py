from pokemon_class import Pokemon
from pokemon_class import Attack
from character_class import Trainer
from character_class import Enemy
from validate import Validate
from battle import Battle
from location_class import Location
from ascii import *



flamethrower = Attack("Flamethrower", 40)
fire_blast = Attack("Fire Blast", 50)
waterfall = Attack("Waterfall", 40)
hydro_pump = Attack("Hydro Pump", 50)
giga_drain = Attack("Giga Drain", 40)
solar_beam = Attack("Solar Beam", 50)
wing_attack = Attack("Wing Attack", 35)
drill_peck = Attack("Drill Peck", 40)
fly = Attack("Fly", 50)
tackle = Attack("Tackle", 30)
scratch = Attack("Scratch", 35)
rapid_spin = Attack("Rapid Spin", 35)
slash = Attack("Slash", 35)
mega_punch = Attack("Mega Punch", 35)
tri_attack = Attack("Tri Attack", 40)
hyperbeam = Attack("Hyperbeam", 55)
feint_attack = Attack("Feint Attack", 35)
pay_back = Attack("Pay Back", 40)
crunch = Attack("Crunch", 40)
thunder_bolt = Attack("Thunder Bolt", 35)
thunder = Attack("Thunder", 50)
high_jump_kick = Attack("High Jump Kick", 50)
confusion = Attack("Confusion", 40)
psychic = Attack("Psychic", 60)
psybeam = Attack("Psybeam", 50)
sludge_bomb = Attack("Sludge Bomb", 40)
acid = Attack("Acid", 40)
ice_punch = Attack("Ice Punch", 35)
ice_beam = Attack("Ice Beam", 50)
play_rough = Attack("Play Rough", 40)


#
persian_attacks = [scratch, play_rough, feint_attack, pay_back]
mewtwo_attacks = [psychic, confusion, tri_attack, ice_beam]
koffing_attacks = [sludge_bomb, pay_back, acid, tackle]
houndoom_attacks = [fire_blast, crunch, feint_attack, flamethrower]
murkrow_attacks = [wing_attack, drill_peck, tackle, pay_back]
arbok_attacks = [sludge_bomb, crunch, acid, feint_attack]
grimer_attacks = [acid, feint_attack, tackle, scratch]
raticate_attacks = [slash, feint_attack, tackle, scratch]

# Pokemon attack list
charizard_attacks = [flamethrower, wing_attack, slash, fire_blast]
blastoise_attacks = [hydro_pump, waterfall, rapid_spin, crunch]
venusaur_attacks = [solar_beam, sludge_bomb, acid, giga_drain]
alakazam_attacks = [confusion, psybeam, tri_attack, flamethrower]
snorlax_attacks = [hyperbeam, mega_punch, ice_punch, crunch]
gyarados_attacks = [hydro_pump, waterfall, drill_peck, crunch]
machamp_attacks = [high_jump_kick, mega_punch, pay_back, ice_punch]
electabuzz_attacks = [thunder, thunder_bolt, slash, play_rough]
pidgeot_attacks = [wing_attack, drill_peck, slash, fly]

# Enemy Pokemon
persian = Pokemon("Persian", 130, 130, persian_attacks)
mewtwo = Pokemon("Mewtwo", 150, 140, mewtwo_attacks)
koffing = Pokemon("Koffing", 120, 120, koffing_attacks)
houndoom = Pokemon("Houndoom", 130, 130, houndoom_attacks)
murkrow = Pokemon("Murkrow", 120, 120, murkrow_attacks)
arbok = Pokemon("Arbok", 130, 130, arbok_attacks)
grimer = Pokemon("Grimer", 110, 110, grimer_attacks)
raticate = Pokemon("Raticate", 120, 120, raticate_attacks)

# User Pokemon
charizard = Pokemon("Charizard", 110, 110, charizard_attacks)
blastoise = Pokemon("Blastoise", 125, 125, blastoise_attacks)
venusaur = Pokemon("Venusaur", 125, 125, venusaur_attacks)
alakazam = Pokemon("Alakazam", 110, 110, alakazam_attacks)
snorlax = Pokemon("Snorlax", 170, 170, snorlax_attacks)
gyarados = Pokemon("Gyarados", 120, 120, gyarados_attacks)
machamp = Pokemon("Machamp", 120, 120, machamp_attacks)
electabuzz = Pokemon("Electabuzz", 120, 120, electabuzz_attacks)
pidgeot = Pokemon("Pidgeot", 120, 120, pidgeot_attacks)


pokemon_party = []
options = [charizard, blastoise, venusaur, alakazam, snorlax, gyarados, machamp, electabuzz, pidgeot]

trainer_name = input("Enter a name ")
sean = Enemy("Team Rocket Leader Sean", "Sean: Spelling isn't your only nemesis today.", [persian, mewtwo])
sampai = Enemy("Rocket Grunt Sam-pai", "Sam-pai: You're going nowhere! I've got you for 3 minutes.", [murkrow, arbok])
zachary = Enemy("Rocket Grunt Zachary", "Zachary: Finally, something to do.", [koffing, houndoom])
trainer = Trainer(trainer_name, pokemon_party, "Union Cave")

# Location Options
union_cave_options = ["Ecruteak City"]
ecruteak_city_options = ["Pokemon Center", "Route 34", "Slowpoke Well", "Enter house with garden"]
pokemon_center_options = ["Ecruteak City"]
old_man_options = ["Ecruteak City"]
route_34_options = ["Battle trainer on the left", "Battle trainer on the right", "Ecruteak City"]
slowpoke_well_options = ["Walk deeper into well", "Ecruteak City"]
main_room_options = ["Explore down the ladder", "Explore crack in the wall","Try the large metal door", "Slowpoke Well"]
grunt_office_options = ["Battle Team Rocket Grunt", "Back to Slowpoke Well Entrance"]
cracked_wall_options = ["Battle Team Rocket Grunt", "Back to Slowpoke Well Entrance"]
sean_office_options = ["Ladder leading out to Ecruteak City", "Battle Team Rocket Leader"]



# Locations
union_cave = Location("Union Cave", union_cave_options, "After several hours of wandering about, you finally navigate your way out of the dark, tricky cave. Ahead of you is a sign: Ecruteak City - 500 feet")
ecruteak_city = Location("Ecruteak City", ecruteak_city_options, "You're in Ecruteak City. Birds are chirping and life is good.")
pokemon_center = Location("Pokemon Center", pokemon_center_options, "You walk into the Pokemon Center. Nurse Joy greets you")
old_man = Location("Old man", old_man_options, "Old man: Hello youngster. Are you new to town? Keep a close eye on your pokemon, strange things have been happening around town lately.")
route_34 = Location("Route 34", route_34_options, "You leave the city and are now on Route 34. There are trainers all around you battling")
slowpoke_well = Location("Inside Slowpoke Well", slowpoke_well_options, "You are now inside the slowpoke well. The inside is a lot larger than you imagined. It has dim lighting and feels humid")
main_room = Location("Deep Inside Slowpoke Well", main_room_options, "You are deep inside the well. You notice a ladder to your right leading down, and a fairly large crack in the wall to your left.")
grunt_office = Location("Grunt Office", grunt_office_options, "You descend down the ladder and find yourself inside a room that looks like an office. There are slowpokes in the corner, each missing their tails. You spot a Team Rocket member at the end of the room, but he has yet to spot you.")
cracked_wall = Location("Crack in the wall", cracked_wall_options, "You crawl through the crack in the wall and emerge into a large area. There are dozens of slowpoke hanging by a small body of water. You notice a Team Rocket member pushing a large cart.")
sean_office = Location("Sean's office", sean_office_options, "You enter the room. Inside, you find the man in charge of the entire operation. He notices you, but does not react.")














def choose_pokemon(trainer, choices):
  count = 0
  while len(choices) > count:
    print(f'{count + 1}. {choices[count].name}')
    count += 1
  user_input = Validate().range(1, len(choices), "please enter a valid option. ", "Select a pokemon you would like to add to your party. ")
  trainer.pokemon_party.append(choices[user_input - 1])
  print(f'You chose {choices[user_input - 1].name}!')
  choices.remove(choices[user_input - 1])
  input("Press enter to continue")
  print("\033c")



def current_location(location):
  print(f'Current Location: {location.name}\n')
  print(f'{location.description}\n\n')
  count = 0
  while count < len(location.options):
    print(f'{count + 1}. {location.options[count]}')
    count += 1
  location_choice = Validate().range(1, len(location.options), "Please choose a valid option", "Where would you like to go? ")
  trainer.location = location.options[location_choice - 1]
  print("\033c")


def play_game():
  logo_img()
  input("Press enter to continue")
  print("\033c")
  choose_pokemon(trainer,options)
  choose_pokemon(trainer,options)
  choose_pokemon(trainer,options)
  while True:
    if trainer.location == 'Union Cave':
      current_location(union_cave)

    elif trainer.location == 'Ecruteak City':
      current_location(ecruteak_city)

    elif trainer.location == 'Pokemon Center':
      current_location(pokemon_center)

    elif trainer.location == "Enter house with garden":
      current_location(old_man)

    elif trainer.location == 'Route 34':
      current_location(route_34)

    elif trainer.location == 'Slowpoke Well':
      current_location(slowpoke_well)

    elif trainer.location == "Back to Slowpoke Well Entrance":
      current_location(main_room)
    
    elif trainer.location == "Walk deeper into well":
      current_location(main_room)
    
    elif trainer.location == "Explore down the ladder":
      current_location(grunt_office)
    
    elif trainer.location == "Explore crack in the wall":
      current_location(cracked_wall)

    elif trainer.location == "Try the large metal door":
      current_location(sean_office)
    
    elif trainer.location == "Ladder leading out to Ecruteak City":
      current_location(ecruteak_city)



play_game()


# current_location(location)
# # Player chooses 3 pokemon
# choose_pokemon(trainer, options)
# choose_pokemon(trainer, options)
# choose_pokemon(trainer, options)

# sean_battle = Battle(trainer, sean)
# sean_battle.battle()

