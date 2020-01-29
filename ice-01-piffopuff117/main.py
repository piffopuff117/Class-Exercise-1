#!/usr/bin python3.8
import random
"""Class has player information."""
class Player:
    def __init__(self, pName, pType, pLevel):
        self.pName = pName
        self.pType = pType
        self.pLevel = pLevel
    
    def pPrint(self):
        print("Name: " + self.pName)
        print("Type: " + self.pType)
        print("Level: " + str(self.pLevel))

player_norm = Player("player", "default", 0)
print("The default player is: ")
player_norm.pPrint()
p1_level = random.randint(1,99)
p2_level = random.randint(1,99)
print("The following player's levels are random")
player_one = Player("player 1", "default", p1_level)
print("player 1 stats: ")
player_one.pPrint()
player_two = Player("player 2", "default", p2_level)
print("player 2 stats: ")
player_two.pPrint()
if p1_level > p2_level:
    print("player 1 has a higher level ")
elif p1_level < p2_level:
    print("player 2 has a higher level ")
else:
    print("They have equal levels ")

    