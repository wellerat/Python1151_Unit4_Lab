"""
Player Class of Match Coins Game

Description:

Author:
    Ann Cooper

Starter Code:
    No Starter Code

Date:
    Sept. 21, 2026
"""

from coin import Coin
class Player:
    """ This class represents a player"""

    def __init__(self, name):
        """Initialize attributes of the Player"""
        self.name = name
        self.wallet = 20
        self.coin = Coin()

    def toss_coin(self):
        """ This method tells the player's coin to toss itself"""
        self.coin.toss()

    def get_coin_side(self):
        """This method gets the side of the payer's coin by calling the coin's get_sideup() method and retuning its value"""
        return self.coin.get_sideup()

    def win_coin(self):
        """Adds 1 to the wallet"""
        self.wallet = self.wallet + 1

    def lose_coin(self):
        """Subtracts 1 from the wallet"""
        self.wallet = self.wallet - 1 

    def get_wallet(self):
        """Returns the current value of wallet"""
        return self.wallet

    def get_name(self):
        """Returns the current value of name"""
        return self.name
        pass
        