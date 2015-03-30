import random

class ChoiceTranslations:
	"""
	Choose the correct translation
	from the options
	"""
	def __init__(self, dict):
		self.forDel = []
		self.keysList = []
		for key in dict:
			self.keysList += [key]
		random.shuffle(self.keysList)
	def num_options(self, choice): # The number of proposed options			
		if int(choice) >= 6:       # should be not more than six	
			self.numOptions = 6
		else:
			self.numOptions = int(choice)
	def translate_out(self, theList):
		supStr = ''
		for translate in theList:				
			supStr += translate + ', '
		supStr = supStr[0:-2]
		return supStr
	def right_option(self, rightOption):
		self.options = []
		self.options += [rightOption]
	def del_right_option(self, key, dict):
		self.wrongDict = dict.copy()
		del self.wrongDict[key]
	def add_wrong_translations(self, wrongDict):
		for word in wrongDict:
			self.options += [wrongDict[word]]
	def output_translations(self, translate_out):
		self.options = self.options[0:self.numOptions]
		supList = []
		for key in self.options:
			supList += [translate_out(key[0:-2])]
		self.options = supList
		random.shuffle(self.options)
		i = 0
		for key in self.options:
			print(str(i + 1) + '.) ', key)
			i += 1 
	def wrong_in_end(self):
		self.keysList += [self.keysList[0]]
		del self.keysList[0]
	def compare_option(self, choice, value, 
					   key, translate_out,
					   wrong_in_end,
					   custom_dict, customDict):
		choice = [self.options[int(choice) - 1]]
		if ', ' in choice[0]:
			num = choice[0].find(', ')
			choice = choice[0][0:num]
		else:
			choice = choice[0]
		if choice in value:
			self.forDel += [key]
		else:
			supStr = translate_out(value[0:-2])
			print("\tIt's wrong!\n", key, ' - ', supStr)
			input()
			wrong_in_end()
			custom_dict(customDict, key)
	def del_right_answers(self):
		if self.forDel != []:
			del self.keysList[0]
		self.forDel = []


class ChoiceWords(ChoiceTranslations):
	"""
	Choose the correct word
	from the options
	"""
	def __init__(self, dict):
		ChoiceTranslations.__init__(self, dict)
	def add_wrong_words(self, wrongDict):
		for word in wrongDict:
			self.options += [word]
	def output_words(self):
		self.options = self.options[0:self.numOptions]
		random.shuffle(self.options)
		i = 0
		for key in self.options:
			print(str(i + 1) + '.) ', key)
			i += 1
	def compare_option(self, choice, key, 
		               supStr, wrong_in_end,
		               custom_dict, customDict):
		choice = [self.options[int(choice) - 1]]
		if choice[0] == key:
			self.forDel += [key]
		else:
			print("\tIt's wrong!\n", key, ' - ', supStr)
			input()
			wrong_in_end()
			custom_dict(customDict, key)

		
		