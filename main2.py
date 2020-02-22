import generators as fn
import random as rnd
import pandas as pd
from faker import Faker

# Initialize the Faker library
fk = Faker()

# Import Data from /data as pandas csv dataframes
# import for functions as lists
abilities = pd.read_csv('data/Abilities.csv')
justifyVariable = 14
background = pd.read_csv('data/SocialClass.csv')
bck = background.columns.str.replace(
    '(\.\d+)$', '').values  # unmangle duplicates
profession = pd.read_csv('data/Professions.csv')
prf = profession.columns
drive = pd.read_csv('data/Drive.csv')
drv = drive.columns


# generate everything!


charName = fk.name()
classRoll = bck[fn.rd6()-1]
background = list(background[classRoll])[fn.rd6()-1]
# currently rolls Profession in same Social Class, not below
profAvailable = list(prf[:list(prf).index(classRoll)+1])
professionChosen = profession[rnd.choice(profAvailable)][fn.rd6()-1]


profDifference = profAvailable.__len__() - profession.columns.get_loc(
    [col for col in profession.columns if profession[col].str.contains(professionChosen).any()][0])-1

# PRINT OUT


print("===BASIC".rjust(justifyVariable), "INFO===")
print('Name:'.rjust(justifyVariable), charName)
print('Background:'.rjust(14), classRoll+'/'+background)
print("Available Profession Levels: " + str(profAvailable))
print('Profession:'.rjust(14), professionChosen, profDifference)

print('Drive:'.rjust(14), drive[drv[int(fn.rd6() > 3)]][fn.rd6()])
print("===ABILI".rjust(justifyVariable)+"TIES===")

for a in abilities.columns:
    roll = fn.r3d6()
    print((a+':').rjust(14), str(roll[1]
                                 ).rjust(2), "(%+d)" % fn.modifier(roll[1]))
    # print('Focuses:'.rjust(14), ', '.join(list(abilities[a].dropna())))

print('Resources:'.rjust(14))
