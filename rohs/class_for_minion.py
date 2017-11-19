class minion(object):
    minion_list = list()
    def __init__(self, name, health, damage, earth, fire, wind, water, lightning, race = None, stealth = False, poison = False, taunt = False, charge = False, rush = False, battlecry = None, deathrattle = None):
        self.name 	          = name
        self.health               = health
        self.damage               = damage
        self.earth                = earth
        self.fire                 = fire
        self.wind                 = wind
        self.water                = water
        self.lightning            = lightning
        self.race                 = race
        self.stealth              = stealth
        self.poison               = poison
        self.taunt                = taunt
        self.charge               = charge
        self.rush                 = rush
        self.battlery             = battlecry
        self.deathrattle          = deathrattle
        self.played               = False
        self.owner                = None
        
        if self.health <= 0:
            death()
            
        if self.played = True:
            if self.battlecry is not None:
                self.battlecry
                       
        def death():
            x = self.owner
            x.field.remove(self)
            if self.deathrattle is not None:
                return self.deathrattle 
