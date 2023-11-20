import sys
import random

print("let's play rock, paper, scissor")
player_choice = input('enter\n 1.for rock\n 2.for paper\n 3.for scissor:\n ')

player = int(player_choice)
print("player choice: ", player)

if player < 1 or player > 3:
    sys.exit("please enter 1, 2 or 3") #Using sys module to exit the code and display the error to the user.

computer_choice = random.choice("123")  #Using random function to generate a random value.

computer = int(computer_choice)
print("computer choice: ", computer)

# All the condition required for the result

def result():    #function to declare a result.
    print("😒 computer wins")

if player == computer :    
    print("😗 it's a draw")

elif player == 1 and computer == 2 :
    result()
elif player == 2 and computer == 3 :
    result()
elif player == 3 and computer == 1 :
    result()

else :
    print("😍 👌 player wins!!!")
