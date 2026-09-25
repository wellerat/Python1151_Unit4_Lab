"""
Coin Class of Match Coins Game

Description:

Author:
    Ann Cooper

Starter Code:
    No Starter Code

Date:
    Sept. 21, 2026
"""
import random

class Coin:
    """This class represents a single, tossable coin.  """

    def __init__(self):
        """Initialize the attributes of coin"""
        self.sideup = "Heads"

    def toss(self):
        """ Generates a random number (0 or 1) """
        value = random.randint(0,1)
        if value == 1:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        """ Returns the value of sideup"""    
        return self.sideup