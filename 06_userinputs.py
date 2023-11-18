#Let,s understand user inputs by building rock, paper, scissor.
import sys
print("let's play rock, paper, scissor")
player_choice = input('enter\n 1.for rock\n 2.for paper\n 3.for scissor\n ')
player = int(player_choice)
if player < 1 or player > 3:
    sys.exit("please enter 1, 2 or 3")