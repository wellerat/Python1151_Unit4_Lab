"""
Match Coins Game

Description:

Author:
    Ann Cooper

Starter Code:
    No Starter Code

Date:
    Sept. 21, 2026
"""

from player import Player

def main():
    """This is the main entry point of Match Coins Game"""

    continue_game = True


    print("\n--- Coin Match Game ---")

    p1 = Player("1")
    p2 = Player("2")

    print(f"Player {p1.get_name()} has {p1.get_wallet()} coins")
    print(f"Player {p2.get_name()} has {p2.get_wallet()} coins")

    while continue_game:

        coin_toss = input("\nDo you want to toss the coins? (y/n):  ").lower()

        if coin_toss == 'y':
            print("\nTossing....")

            p1.toss_coin()
            p2.toss_coin()

            print(f"Player {p1.get_name()} tossed {p1.get_coin_side()} ")
            print(f"Player {p2.get_name()} tossed {p2.get_coin_side()}")

            if p1.get_coin_side() != p2.get_coin_side():
                print(f"\n...No Match! Player {p2.get_name()} wins a coin")

                p2.win_coin()
                p1.lose_coin()

            else:    
                print(f"\n...Match! Player {p1.get_name()} wins a coin")

                p1.win_coin()
                p2.lose_coin()

            print(f"Player {p1.get_name()} has {p1.get_wallet()} coins")
            print(f"Player {p2.get_name()} has {p2.get_wallet()} coins")

        elif coin_toss == 'n':
            print("---   Final Score   ---")
            print(f"Player {p1.get_name()}:  {p1.get_wallet()}")
            print(f"Player {p2.get_name()}:  {p2.get_wallet()}")

            if p1.get_wallet() > p2.get_wallet():
                print(f"Player {p1.get_name()} wins!")
            elif p1.get_wallet() < p2.get_wallet():
                print(f"Player {p2.get_name()} wins!")
            else:
                print("It's a draw!")            

            continue_game = False

        else:
            print("Invalid entry...")   


main()