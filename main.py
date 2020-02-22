import pandas as pd
import random as rnd
from Ability import Ability
from Bio import Bio

abilities = pd.read_csv('./data/Abilities.csv')


# for abi in abilities.columns:
#     a = Ability(abi)
#     print(a.name, a.value, "(%+d)" % a.modifier)
#     a.addFocus(rnd.choices(
#         a.availableFocuses, k=2))
#     print('Focuses:', a.getFocusList())


b = Bio()
print(b.name)
print(b.socialClass+'/'+b.background)
print(b.profession)
print(b.professionAdvantage)
print(b.drive)
