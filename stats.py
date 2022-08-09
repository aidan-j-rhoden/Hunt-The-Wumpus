#!/usr/bin/env python3.10

from random import choice

player = 19 #What room the player starts in.
crookedArrows = 5 #How many arrows you have

#The positions of the other things.
wumpus = choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20]) #There's probablly a more elegant way to do this, but I didn't find it.
superBat1 = choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20])
superBat2 = choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20])
bottomlessPit1 = choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20])
bottomlessPit2 = choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20])
