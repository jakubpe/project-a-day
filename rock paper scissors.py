import random
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
Paper
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
RPS = [rock, paper, scissors]
player = int(input("Rock, paper, scissors game. To pick Rock type in '0', to pick paper type in '1', to pick scissors type in '2'\n"))
if player in [0, 1, 2]:
    computer = random.randint(0, 2)
    print("You picked" + RPS[player] + "\nComputer picked:" + RPS[computer])
    #if player == computer:
    #   print("Draw")
    #possible game logic; but lets try something different
    # else:
        # if player == 0 :
    #         if computer == 1:
    #             print("Computer wins")
    #         else:
    #             print("You win")
    #     elif player == 1:
    #         if computer == 0:
    #             print("You win")
    #         else:
    #             print("Computer wins")
    #     else:
    #         if computer == 0:
    #             print("Computr wins")
    #         else:
    #             print("You win")
    if player == computer:
        print("Draw")
    elif (player == 0 or computer == 0) and (player == 2 or computer == 2):
        if player == 0:
            print("User wins")
        else:
            print("Computer wins")
    elif computer > player:
        print("Computer wins")
    elif player > computer:
        print("User wins")
else:
    print("Incorrect choice, computer wins")



