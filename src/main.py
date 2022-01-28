from type import Type, Pokemon, Team

normal = Type('Normal')
fighting = Type('Fighting')
flying = Type('Flying')
poison = Type('Poison')
ground = Type('Ground')
rock = Type('Rock')
bug = Type('Bug')
ghost = Type('Ghost')
steel = Type('Steel')
fire = Type('Fire')
water = Type('Water')
grass = Type('Grass')
electric = Type('Electric')
psychic = Type('Psychic')
ice = Type('Ice')
dragon = Type('Dragon')
dark = Type('Dark')
fairy = Type('Fairy')

all_types = [normal, fighting, flying, poison, ground, rock,
            bug, ghost, steel, fire, water, grass,
            electric, psychic, ice, dragon, dark, fairy]

normal.weak = [fighting]
normal.resistance = [] 
normal.immune = [ghost]
normal.double = []
normal.half = [rock, steel]
normal.zero = [ghost]

fighting.weak = [flying, psychic, fairy]
fighting.resistance = [rock, bug, dark] 
fighting.immune = []
fighting.double = [normal, rock, steel, ice, dark]
fighting.half = [flying, poison, bug, psychic, fairy]
fighting.zero = [ghost]

flying.weak = [rock, electric, ice]
flying.resistance = [fighting, bug, grass] 
flying.immune = [ground]
flying.double = [fighting, bug, grass]
flying.half = [rock, steel, electric]
flying.zero = []

poison.weak = [ground, psychic]
poison.resistance = [fighting, poison, bug, grass, fairy] 
poison.immune = []
poison.double = [grass, fairy]
poison.half = [poison, ground, rock, ghost]
poison.zero = [steel]

ground.weak = [water, grass, ice]
ground.resistance = [poison, rock] 
ground.immune = [electric]
ground.double = [poison, rock, steel, fire, electric]
ground.half = [bug, grass]
ground.zero = [flying]

rock.weak = [fighting, ground, steel, water, grass]
rock.resistance = [normal, flying, poison, fire] 
rock.immune = []
rock.double = [flying, bug, fire, ice]
rock.half = [fighting, ground, steel]
rock.zero = []

bug.weak = [flying, rock, fire]
bug.resistance = [fighting, ground, grass] 
bug.immune = []
bug.double = [grass, psychic, dark]
bug.half = [fighting, flying, poison, ghost, steel, fire, fairy]
bug.zero = []

ghost.weak = [ghost, dark]
ghost.resistance = [poison, bug] 
ghost.immune = [normal, fighting]
ghost.double = [ghost, psychic]
ghost.half = [dark]
ghost.zero = [normal]

steel.weak = [fighting, ground, fire]
steel.resistance = [normal, flying, rock, bug, steel, grass, psychic, ice, dragon, fairy] 
steel.immune = [poison]
steel.double = [rock, ice, fairy]
steel.half = [steel, fire, water, electric]
steel.zero = []

fire.weak = [ground, rock, water]
fire.resistance = [bug, steel, fire, grass, ice, fairy] 
fire.immune = []
fire.double = [bug, steel, grass, ice]
fire.half = [rock, fire, water, dragon]
fire.zero = []

water.weak = [grass, electric]
water.resistance = [steel, fire, water, ice] 
water.immune = []
water.double = [ground, rock, fire]
water.half = [water, grass, dragon]
water.zero = []

grass.weak = [flying, poison, bug, fire, ice]
grass.resistance = [ground, water, grass, electric] 
grass.immune = []
grass.double = [ground, rock, water]
grass.half = [flying, poison, bug, steel, fire, grass, dragon]
grass.zero = []

electric.weak = [ground]
electric.resistance = [flying, steel, electric] 
electric.immune = []
electric.double = [flying, water]
electric.half = [grass, electric, dragon]
electric.zero = [ground]

psychic.weak = [bug, ghost, dark]
psychic.resistance = [fighting, psychic] 
psychic.immune = []
psychic.double = [fighting, poison]
psychic.half = [steel, psychic]
psychic.zero = [dark]

ice.weak = [fighting, rock, steel, fire]
ice.resistance = [ice] 
ice.immune = []
ice.double = [flying, ground, grass, dragon]
ice.half = [steel, fire, water, ice]
ice.zero = []

dragon.weak = [ice, dragon, fairy]
dragon.resistance = [fire, water, grass, electric] 
dragon.immune = []
dragon.double = [dragon]
dragon.half = [steel]
dragon.zero = [fairy]

dark.weak = [fighting, bug, fairy]
dark.resistance = [ghost, dark] 
dark.immune = [psychic]
dark.double = [ghost, psychic]
dark.half = [fighting, dark, fairy]
dark.zero = []

fairy.weak = [poison, steel]
fairy.resistance = [fighting, bug, dark] 
fairy.immune = [dragon]
fairy.double = [fighting, dragon, dark]
fairy.half = [poison, steel, fire]
fairy.zero = []

def main():
    team = Team(Pokemon([fighting, fire]),
                Pokemon([normal, flying]),
                Pokemon([electric]),
                Pokemon([psychic, steel]),
                Pokemon([water]),
                Pokemon([dark, poison]))

    print('Double damage coverage: ')
    for type in team.double:
        print(type)

    print('\n\n--------------------------------------------------------\n\n')

    print('Types lacking double damage: ')
    for type in all_types - team.double:
        print(type)

    print('\n\n--------------------------------------------------------\n\n')
    
    print('Resistance + Immunity coverage: ')
    for type in set(team.resistance + team.immune):
        print(type)

    print('\n\n--------------------------------------------------------\n\n')

    print('Types lacking resistance + immunity: ')
    for type in all_types - (team.resistance + team.immune):
        print(type)