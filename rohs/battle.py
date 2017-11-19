from minions import minion
from player import Player1
from player import Player2

def summon_minion(player, minion):
    if minion in player.hand:
        playable = True
        elements = ['earth', 'fire', 'wind', 'water', 'lightning']             
        for i in elements:
            x = getattr(player, i)
            y = getattr(minion, i)
            print(x)
            print(y)
            if x - y >= 0:
                x = x - y
            else:
                playable = False
    if playable == True:
        setattr(minion, 'played', True)
        setattr(minion, 'owner', player)
        return player.field.append(minion)
    else:
        return "You don't have enough devotion"
        
def get_target_list(opponent):
    target_list = list()
    for i in opponent.field:
        if hasattr(i, 'taunt'):
            i.append(target_list)
    if target_list == ():
        target_list = target_list.extend(opponent.field)
    else:
        pass
    return target_list      
