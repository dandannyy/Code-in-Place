import random

"""
Can you write an AI opponent? You can start with a dumm AI
that always plays a random number.
+ Other idea: Divible by 3 rule: if the number of stones remaining at the
end of a player's turn is divisible by 3, they must go again. 
"""

def main():
    stones = 20
    player = 1
    mode = input("Play against AI? (yes/no): ") # Switch for AI opponent?
    while stones > 0:
        print(f"There are {stones} stones left.")
        if mode == "yes" and player == 2:
            if stones % 3 == 0:
                move = random.randint(1, 2)
            else:
                move = stones % 3
            if stones == 1:
                move = 1
                print (f"AI removes {move} stones.")
        else:
            move = int(input(f"Player {player}, remove 1 or 2: "))
            while move != 1 and move != 2:
                move = int(input("Please enter 1 or 2: "))
            while stones == 1 and move != 1:
                move = int(input("Only 1 stone left! Please enter1 : "))
        stones = stones - move
        print()
        # if game over the winner it's the other player
        if stones <= 0:
            if player == 1:
                winner = 2
            else:
                winner = 1
        else:
            if stones % 3 == 0: # Other idea
                print(f"{stones} is divible by 3!")
                print(f"Player {player} gets another turn!")
            else:
                #switch player, if the games continue
                if player == 1:
                    player = 2
                else:
                    player = 1  
    print(f"Player {winner} wins!")

if __name__ == '__main__':
    main()
