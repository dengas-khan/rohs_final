class class_for_spell(object):
	
	spell_list = list() 
	
	def __init__(self, hero=False, minion=False, name=None, imgfile = None, damage=None, targeted=False, heal=None, card_draw = None, minion_summon=None, buff=False, destroy=False, special_ability=None):
		
		
		
		self.hero            = hero
		self.minion          = minion
		self.name            = name
		self.imgfile         = imgfile
		self.damage          = damage
		self.targeted        = targeted
		self.heal            = heal
		self.card_draw 	     = card_draw
		self.minion_summon   = minion_summon
		self.buff            = buff
		self.destroy         = destroy
		self.special_ability = special_ability
		
		
		if not self.name==None: self.spell_list.append(self.name)
	
	
	def return_attr(self):
		"""will return if the spell is targeted, and 
		   if it does damage"""
		   
		  
		print(self.damage)
		damage = bool()
		if self.heal == None: heal = False
		else: heal = self.heal
		if self.damage ==None: damage=False
		else: damage = self.damage
		
		
		return (self.minion, self.hero, self.targeted, heal, damage)
	
	
	
		
