import random as rnd
import generators as gen
import pandas as pd

abilities = pd.read_csv('./data/Abilities.csv')


class Ability(object):
    # Constructor
    def __init__(self, name):
        self.name = name
        self.value = gen.r3d6()[1]
        self.modifier = gen.modifier(self.value)
        self.availableFocuses = [
            f for f in abilities[self._name] if str(f) != 'nan']
        self.focusList = []

#Properties, getters/setters

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def focusList(self):
        return self._focusList

    @focusList.setter
    def focusList(self, f):
        self._focusList = f

# Class methods

    def addFocus(self, f):
        self.focusList = self.focusList + f
        return self.focusList

    def changeModifier(self, v):
        self.modifier += v

    def getFocusList(self):
        return {focus: self.focusList.count(focus) for focus in self.focusList}
