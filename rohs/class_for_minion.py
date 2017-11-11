class class_for_minion(object):
	
	minion_list = list()
	
	def __init__(self, name=None, image_file=None, health=None, damage=None, devotiontype=None, devotioncost=None, stealth = False, poison = False, taunt = False, storm = False, battlecry=None, deathrattle=None, special_ability=None, passive=None):
		"""deathrattle, special_ability, battlecry, and 
		   passive all need to be functions"""
		   
		   
		self.health           = health
		self.damage           = damage
		self.attribute        = attribute
		self.stealth          = stealth
		self.poison           = poison
		self.taunt            = taunt
		self.storm            = storm
		self.battlecry        = battlecry
		self.deathrattle      = deathrattle
		self.speacial_ability = special_ability
		self.name 			  = name
		self.image_file       = image_file
		
		
		if not self.name==None: self.minion_list.append(self.name)
			
			
	def return_special_attributes(self):
		"""will return if the minion is poisonous or
		   stealthy in a tuple, for stealth, the other minion 
		   will attack, and then if the other minion has stealth, 
		   the damage will not be taken away"""
		   
		   
		return (self.stealth, self.poison, self.taunt, self.storm)
	
	
	def execute_battlecry(self):
		"""executes the battlecry"""
		
		
		return self.battlecry
	
	
	def execute_deathreattle(self):
		"""executes the deathrattle"""
		
		
		return self.deathrattle
	
	
	def execute_special_ability(self):
		"""executes the special ability"""
		
		
		return self.special_ability
	
	
	def exectue_passive(self):
		"""executes the passive"""
		
		
		return self.passive
	
	
	def return_image_file(self):
		"""returns the image file"""
	
	
		return self.image_file
		
