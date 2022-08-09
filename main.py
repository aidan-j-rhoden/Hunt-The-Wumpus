#!/usr/bin/env python3.10

from subprocess import run
from random import randint, choice
from time import sleep

from rooms import getRooms
import stats

run("clear")



def intro(stats):
    input("Welcome to 'Hunt the Wumpus!' (hit enter to continue)")
    input("\nYou have chosen to hunt the evil Wumpus.  The Wumpus lives in a cave made up of a maze of 20 rooms.\nEach room has three tunnels connecting to another room.")
    input("\nBut be careful!  There are known to be drafty bottomless pits in this cave, and rustling super bats that might carry you off into the cave.")
    input("\nThankfully, you are armed with your trusty bow and five (5) crooked arrows.  All you have to do is aim the arrow into a room, and it will fly crooked and true through the other rooms.")
    print("\nGood luck!")
    sleep(2)
    run("clear")
    main(stats)

def main(stats):
    while True:
        if stats.wumpus == stats.player:
            print("The Wumpus got you!!")
            break
        if stats.bottomlessPit1 == stats.player or stats.bottomlessPit2 == stats.player:
            print("You fall into a bottomless pit.")
            break
        if stats.superBat1 == stats.player: 
            print("You startle a super bat.  It picks you up, carries you to a random room, then drops you there and flies off.")
            stats.player = randint(1, 20)
            stats.superBat1 = randint(1, 20)
        elif stats.superBat2 == stats.player:
            print("You startle a super bat.  It picks you up, carries you to a random room, then drops you there and flies off.")
            stats.player = randint(1, 20)
            stats.superBat2 = randint(1, 20)
        print("\nYou are in room {}.  The tunnels branching off go to rooms {}, {}, and {}.".format(stats.player, getRooms(stats.player)[0], getRooms(stats.player)[1], getRooms(stats.player)[2]))
        if stats.superBat1 in getRooms(stats.player) or stats.superBat2 in getRooms(stats.player):
            print("    I hear a bat.")
        if stats.bottomlessPit1 in getRooms(stats.player) or stats.bottomlessPit2 in getRooms(stats.player):
            print("    I feel a draft.")
        if stats.wumpus in getRooms(stats.player):
            print("    I smell a wumpus.")
        result = input("\nShoot or Move? [S-M] ")
        if result.upper() == "M":
            stats.player = int(input("Which room? [{}, {}, {}] ".format(getRooms(stats.player)[0], getRooms(stats.player)[1], getRooms(stats.player)[2])))
            continue
        elif result.upper() == "S":
            shoot(stats)

def shoot(stats):
    if stats.crookedArrows != 0:
        while True:
            try:
                distance = int(input("How far do you want to shoot the arrow? [1-5] "))
                assert 0 < distance < 6
                break
            except:
                continue
        while True:        
            try:
                direction = int(input("Which room do you want to shoot the crooked arrow into? [{}, {}, {}] ".format(getRooms(stats.player)[0], getRooms(stats.player)[1], getRooms(stats.player)[2])))
                break
            except:
                continue
        if direction not in getRooms(stats.player):
            direction = choice(getRooms(stats.player))
        for i in range(0, distance):
            if i == 0:
                arrow = direction
                cameFrom = arrow
                print("    Your arrow flies into room {}.".format(direction))
            else:
                while True:
                    num = choice(getRooms(arrow))
                    if num == cameFrom: #Don't allow the arrow to turn right around and skewer you.
                        continue
                    else:
                        arrow = num 
                        break
                print("    Your arrow flies into the next room.")
            if arrow == stats.player:
                print("Your stinkin' crooked arrow flew back and hit you.")
                quit()
            if arrow == stats.wumpus:
                print("\nAHA! You got the wumpus!\nHEE HEE HEE - The Wumpus'll get you next time!!")
                quit()
            sleep(0.4)
        print("You missed, you are now minus one arrow, plus you startled the Wumpus.")
        stats.crookedArrows -= 1
        stats.wumpus = choice(getRooms(stats.wumpus))
        return
    print(choice(["Sorry buster.  You used up all off your crooked arrows.", "Sorry charlie. You're empty."]))
    

if __name__ == "__main__":
    intro(stats)
