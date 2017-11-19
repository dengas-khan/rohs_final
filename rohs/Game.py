import random
from player import Player1
from player import Player2

def gain_devotion(player):
    x = input('Enter which devotion to gain ' + player.name + ': ')
    elements = [player.devotion1, player.devotion2]
    if x in elements:
        y = getattr(player, x)
        return setattr(player, x, y + 1)
    else:
        return gain_devotion(player)       

def draw_card(player):
    x = random.choice(player.deck)
    player.deck.remove(x)
    player.hand.append(x)      
            
def main():
    x = random.randrange(1, 3)
    if x == 1:
        y = gain_devotion(Player1)
    elif x == 2:
        y = gain_devotion(Player2)
    
main() 
