# Week 4 (OPTIONAL)
"""
Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. 
Players alternate taking stones until there are zero left. The game of Nimm goes as follows:
-The game starts with a pile of 20 stones between the players
-The two players alternate turns
-On a given turn, a player may take either 1 or 2 stone from the center pile
-The two players continue until the center pile has run out of stones.

The last player to take a stone loses.
Write a program to play Nimm. To make your life easier we have broken the problem down into smaller milestones. You have a lot of time for this program. Take it slowly, piece by piece.
"""

def main():
    stones = 20
    player = 1
    while stones > 0:
        print(f"There are {stones} stones left.")
        game_mensage = int(input(f"Player {player} would you like to remove 1 or 2 stones? "))
        while game_mensage != 1 and game_mensage !=2:
            game_mensage = int(input("Please enter 1 or 2: "))
        stones = stones - game_mensage
        print()
        # if game over the winner it's the other player
        if stones <= 0:
            if player == 1:
                winner = 2
            else:
                winner = 1
        else:
            #switch player, if the games continue
            if player == 1:
                player = 2
            else:
                player = 1  
    print(f"Player {winner} wins!")

if __name__ == '__main__':
    main()
