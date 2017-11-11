import minion_file, spell_file

"""
this is the file that will make the class for the 
different types of hero, it will not be used when
the players are playing, but will only be used to 
initialize the hero. 
"""


class hero(object):
	classes = list()
	
	
	def __init__(self, health=None, heroname=None, imgfile=None):
		self.health   = health
		self.heroname = heroname
		
		
		if not self.heroname == None: self.classes.append(self.heroname)
	
	
	def return_classes(self):
		"""this will return a list`
		   of all the classes"""

		   
		   
		return self.classes	
	
	
"""
since the images are not available, 
I will just put 'somefile.png as the#
image file parameter
"""

 
Cleric = hero(30, 'Cleric', 'somefile.png')
Knight = hero(40, 'Knight', 'somefile.png')
Sorcerer = hero(25, 'Sorcerer', 'somefile.png')
Demon = hero(35, 'Demon', 'somefile.png')
Hunter = hero(25, 'Hunter', 'somefile.png')



"""
class Sorceror(hero):


	def __init__(self, deck):
		self.deck = (minion_file.bloodfen_raptor(), spell_file.fireball(), etc)
		super().__init__(heroname = 'Sorceror'
				 health = 25
				 imgfile = 'somefile.png')
""" 
				 
	
