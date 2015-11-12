class Musician(object):
	def __init__(self, sounds):
		self.sounds = sounds

	def solo(self, length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end=' ')
		print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
	def __init__(self):
	# Call the __init__ method of the parent class
		super().__init__(["Twang","Thrumb","Bling"])

class Guitarist(Musician):
	def __init__(self):
	# Call the __init__ method of the parent class
		super().__init__(["Boink","Bow","Boom"])

	def tune(self):
		print("Be with you in a moment")
		print("Twoning, sponing, splang")

class Drummer(Musician):
	def __init__(self):
	# Call the __init__ method of the parent class
		super().__init__(["wham","diddle","wham","diddle"])

	def count(self):
		print(
			"""\t\t\ta one\n
			and a two\n
			and a three\n
			and a four"""
			)

	def spontaneouslyCombust(self):
		print(
			"""\t\t\tYou bloody well need a new guitariest\n
			Because I'm about to catch fire!!!!\n"""
			
			)

		try:
			raise NameError("I've Combusted")
		except NameError:
			print("I smell combustion!")
			raise


class Band(object):
	def __init__(self):
	# Request that the new band be given a name
		self.members = dict(drummer='',bassist='',guitarist='')
		self.bandName = ''
		while self.bandName == '':
			self.bandName = input('Please select a band name!')
 
 
	def addMember(memberName,instrument):
		
			
	

			
		
