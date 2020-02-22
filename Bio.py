import generators as gen
import pandas as pd
import random as rnd
from faker import Faker
fk = Faker()

bckg = pd.read_csv('./data/SocialClass.csv')
prfs = pd.read_csv('./data/Professions.csv')
drve = pd.read_csv('./data/Drive.csv')


class Bio(object):
    def __init__(self):
        self.name = fk.name()
        self.age = rnd.randrange(16, 75)
        self.height = rnd.randrange(150, 210)
        self.weight = rnd.randrange(50, 120)
        self.socialClass = bckg.columns.str.replace(
            '(\.\d+)$', '').values[gen.rd6()-1]
        self.background = bckg[self.socialClass][gen.rd6()-1]
        self.profession = prfs[rnd.choice(list(prfs[list(
            prfs.loc[:, :self.socialClass].columns)].columns))][gen.rd6()-1]
        self.professionAdvantage = self.profAboveClass(
            self.socialClass, self.profession)
        self.drive = drve[drve.columns[int(gen.rd6() > 3)]].values[gen.rd6()-1]

# Properties, getters/setters

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        self._age = a

    @property
    def height(self):
        return self._age

    @height.setter
    def height(self, h):
        self._height = h

    @property
    def weight(self):
        return self._age

    @weight.setter
    def weight(self, w):
        self._weight = w

    @property
    def socialClass(self):
        return self._socialClass

    @socialClass.setter
    def socialClass(self, sc):
        self._socialClass = sc

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, bg):
        self._background = bg

    @property
    def profession(self):
        return self._profession

    @profession.setter
    def profession(self, pr):
        self._profession = pr

    @property
    def drive(self):
        return self._drive

    @drive.setter
    def drive(self, dr):
        self._drive = dr

# class methods
    def profAboveClass(self, socclass, prof):
        maxProfClass = prfs.columns.get_loc(socclass)+1
        selProfClass = prfs.columns.get_loc(
            [col for col in prfs.columns if prfs[col].str.contains(prof).any()][0])+1

        return maxProfClass - selProfClass
