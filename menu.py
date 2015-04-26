
class Menu:
	"""docstring for Menu"""
	def zero_print(self):
		print(' 0.) menu')
		print(' -' * 14)
	def minus_one(self):
		print('-1.) back')
	def output_menu_list(self):
		print('-1.) back')
		print(' 0.) add new dictionary')
	def output_menu_dict(self):
		print('-1.) back')
		print(' 0.) add new word')
	def name_newDict(self, theList):
		self.nameNewDict = input('Enter a name for the new dictionary: ')
		self.theList = theList
		self.theList += [[self.nameNewDict, []]]
	def add_newWord(self, newDict):
		self.newDict = newDict
		while True:
			newWord = input('Enter a new word or phrase: ')
			if newWord == '':
				break
			else:
				supList = []
				while True:
					trans = input('Enter a translation: ')
					if trans == '':
						break
					else:
						supList += [trans]
				self.newDict[newWord] = supList + [0, 0]

if __name__ == '__main__':

	insMenu = Menu()

	insMenu.minus_one()
	insMenu.zero_print()
	insMenu.output_menu_list()

		