#! /usr/bin/python3

import random

comp_choice=int(random.randint(0,3))

com_points=0
player_points=0



print("play along")
while(True):

    player_move=int(input("enter 1 for sessior 2 for paper 3 for stone and 99 for exit:  "))

    if player_move == 99:
        print("thanks for playing. have a nice day.")
        break

    if player_move == 1 and comp_choice== 3:
        com_points+=1
        print("you choose sessior while computer choose stone")

    elif player_move == 2 and comp_choice== 1:
        com_points+=1
        print("you choose paper while computer choose sessior")

    elif player_move == 3 and comp_choice== 2:
        com_points+=1
        print("you choose stone while computer choose paper")

    elif player_move == 1 and comp_choice== 2:
        player_points+=1
        print("you choose sessior while computer choose paper")

    elif player_move == 2 and comp_choice== 3:
        player_points+=1
        print("you choose paper while computer choose stone")

    elif player_move == 3 and comp_choice== 1:
        player_points+=1
        print("you choose stone while computer choose sessior")

    elif player_move == comp_choice:
        print("oh!! we chose the same")

    else:
        print("wrong input try again!!!")

    print()
    print()


    print("score: you=",player_points,"computer:",com_points)


    print()
    print()
