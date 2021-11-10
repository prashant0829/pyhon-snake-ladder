import random as r
from playsound import playsound
ladder={5:7, 8:15, 11:18}
snake={6:1, 12:9, 19:3}
player1=0
player2=0
y = True
s = 0
dice=[1,2,3,4,5,6]

def diceroll():
    d = r.choice(dice)
    return d
def snakebite(player):
    a = snake[player]
    player = a
    return player
def ladderclimb(player):
    a = ladder[player]
    player = a
    return player

print("--------> Game started between Player 1 and and Payer 2 <--------")
print("-------->Player 1 and player 2 are on the board<--------")
while y == True:
    print("\n\n---->Player 1 thrown the dice<----")
    dice_value = diceroll()
    playsound("D:\y2mate.com - dice_roll_sound_non_copyrighted_sound_effects_dEHqgEjNsms.mp3")
    print("Player 1 got the number:",dice_value)
    check = dice_value + player1
    if check > 20:
        print("Opps Player 1 Can't move ahead with this dice value")
    else:
        player1 = check
        print("Player 1 is on:", player1)
        if player1 in snake:
            print("Oh no you have been bitten by snake")
            playsound("D:\snakehiss.mp3")
            player1 = snakebite(player1)
            print("Player 1 is demoted to number:", player1)
        elif player1 in ladder:
            print("Congo you climb on the ladder")
            player1 = ladderclimb(player1)
            playsound("D:\y2mate.com - ladder_footsteps_counter_strike_source_sound_effects_for_editing_3m4Ad6DMsQQ.mp3")
            print("Player 1 is promoted  to number:", player1)
        if player1 == 20:
            print("Player 1 won this Match\nGame Over")
            playsound("D:\\applause-2.mp3")
            y = False
            s = 1



    if s == 0:
        print("\n\n---->Player 2 thrown the dice<----")
        dice_value = diceroll()
        playsound("D:\y2mate.com - dice_roll_sound_non_copyrighted_sound_effects_dEHqgEjNsms.mp3")
        print("Player 2 got the number:", dice_value)
        check = player2 + dice_value
        if check > 20:
            print("Opps Player 2 Can't move ahead with this dice value")
        else:
            player2 = check
            print("Player 2 is on:", player2)
            if player2 in snake:
                print("Oh no you have been bitten by snake")
                player2 = snakebite(player2)
                playsound("D:\snakehiss.mp3")
                print("Player 2 is demoted to number:", player2)
            elif player2 in ladder:
                print("Congo you climb on the ladder")
                player2 = ladderclimb(player2)
                playsound("D:\y2mate.com - ladder_footsteps_counter_strike_source_sound_effects_for_editing_3m4Ad6DMsQQ.mp3")
                print("Player 2 is promoted to number:", player2)
            if player2 == 20:
                print("Player 2 won this Match\nGame Over")
                playsound("D:\\applause-2.mp3")
                y = False












