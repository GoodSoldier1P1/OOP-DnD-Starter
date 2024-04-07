import numpy as np

# True universal class

class DiceSet:
    # Define the range of values for dice
    d2 = [x + 1 for x in range(2)]
    d4 = [x + 1 for x in range(4)]
    d6 = [x + 1 for x in range(6)]
    d8 = [x + 1 for x in range(8)]
    d10 =  [x + 1 for x in range(10)]
    d12 = [x + 1 for x in range(12)]
    d20 = [x + 1 for x in range(20)]

    def __init__(self, d2=d2, d4=d4, d6=d6, d8=d8, d10=d10, d12=d12, d20=d20):
        self.d2 = d2
        self.d4 = d4
        self.d6 = d6
        self.d8 = d8
        self.d10 = d10
        self.d12 = d12
        self.d20 = d20

    def ability_check(self, n_dice=1, modifier=0, advantage=False,
                      disadvantage=False):
        # Current total for ability check
        total = 0
        # List of outcomes for advantage or disadvantage rolls
        totals = []
        # Creating Local variable of d10 for ease of use
        d20 = [x + 1 for x in range(20)]
        # Number of rolls performed
        num_rolls = 0
        # Loop to support multiple dice rolls
        while num_rolls < n_dice:
            # Roll d20
            roll = np.random.choice(d20)
            # Inform of Nat 20 or Nat 1 rolls
            if roll == 20:
                print("Nat 20!!!")
            if roll == 1:
                print("Nat 1...")
            # Add skill or item modifiers to roll
            ability = roll + modifier
            # Distinguish between Nat and Mod 20 rolls
            if (ability == 20) and (modifier != 0):
                print("Modified 20")
            # Update roll total
            total += ability
            # Update list of totals for use with Advantage/Disadvantage
            totals.append(ability)
            # Update number of rolls performed
            num_rolls += 1
        # Determine which values to return
        if advantage == True:
            print(totals)
            return f"Rolled: {max(totals)}"
        elif disadvantage == True:
            print(totals)
            return f"Rolled: {min(totals)}"
        else:
            return f"Rolled: {total}"
        
# daniels_dice is an instance of the dice_set class
# daniels_dice = DiceSet()

# Perform ability check with +5 Modifier
# Advantage gives highest dice roll
# Disadvantage gives lowest dice roll, doesn't mean you will fail
# print(daniels_dice.ability_check(n_dice=2, modifier=5, disadvantage=True))


# The Sentient Class
class Sentient(DiceSet):
    def __init__(self, name=None, in_game_name=None, race=None, size=None,
                 alignment=None, armor_class=None, hit_points=None,
                 travel_type=None, speed=None, strength=None, dexterity=None,
                 constitution=None, intelligence=None, wisdom=None,
                 charisma=None, skills={}, passive_perception=None,
                 languages=None, saving_throws={}, roll_modifers={}):
        self.name = name
        self.in_game_name = in_game_name
        self.race = race
        self.size = size
        self.alignment = alignment
        self. armor_class = armor_class
        self.hit_points = hit_points
        self.travel_type = travel_type
        self.speed = speed
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.skills = skills
        self.passive_perception = passive_perception
        self.languages = languages
        self.saving_throws = saving_throws
        self.roll_modifiers = roll_modifers

# Creating instance of universal calss using a monster
boba = Sentient(name='Boba', in_game_name='Aatxe', race='Celestial',
                size='Large', alignment='lawful-good', armor_class=14,
                hit_points=105, travel_type='Walk', speed=50, strength=22,
                dexterity=12, constitution=20, intelligence=10, wisdom=14,
                charisma=14, skills={}, passive_perception=12,
                languages='Understands ALL, Cannot Speak', saving_throws={},
                roll_modifers={})

# Editing roll_modifiers
boba.roll_modifiers = {'str': 6, 'dex': 1, 'con': 5, 'int': 0, 'wis': 2, 'cha': 2}

# Printing
# print("Boba's Modifiers: ", boba.roll_modifiers)
# print(" ")

# Boba rolls for a strength ability check
# strength_ablt_chk = boba.ability_check(modifier=boba.roll_modifiers['str'])
# print("Result of Boba's Strength Ability Check ", strength_ablt_chk)

# Creating a Monster class (child of Sentient) with the ability to use Legendary Actions
class Monster(Sentient):
    def __init__(self, legendary_actions={}):
        self.legendary_actions = legendary_actions
    
    def use_legendary_action(self, legendary_action):
        return "Uses " + legendary_action
    
aatxe = Monster(legendary_actions={'Detect': 'Makes a Wisdom (Perception) check',
                           'Gore': 'The aatxe makes one gore attack (Cost: 2 Actions)',
                           'Bulwark': 'The aatxe flares crimson with celestial power, protecting those nearby. The next attack that would hit an ally within 5 feet of the aatxe hits the aatxe instead'})

print(aatxe.legendary_actions['Bulwark'])

# Character class, sibling of Monster
class Character(Sentient):
    pass
