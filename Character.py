import funcs as fn
import json as js
from faker import Faker
fk = Faker()


class Character(object):
    def __init__(self):
        self.name = fk.name()
        self.abilityAccuracy = fn.r3d6()[1]
        self.abilityConstitution = fn.r3d6()[1]
        self.abilityCommunication = fn.r3d6()[1]
        self.abilityDexterity = fn.r3d6()[1]
        self.abilityFighting = fn.r3d6()[1]
        self.abilityIntelligence = fn.r3d6()[1]
        self.abilityPerception = fn.r3d6()[1]
        self.abilityStrength = fn.r3d6()[1]
        self.abilityWillpower = fn.r3d6()[1]

    def __getattribute__(self, name):
        return object.__getattribute__(self, name)

    def mod(self, val):
        return fn.modifier(val)


c = Character()

print(c.abilityAccuracy, c.mod(c.abilityAccuracy))
