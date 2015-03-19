
import random

class ChoiceVar:
	"""docstring for ChoiceVar"""
	def __init__(self):
		pass
	def num_options(self, choice):				
		if int(choice) >= 6:
			self.numOptions = 6
		else:
			self.numOptions = int(choice)
	def translate_out(self, theList):
		supStr = ''
		for translate in theList:
			supStr += translate + ', '
		supStr = supStr[0:-2]
		return supStr
	def out_word(self, key):
		print('\n', key)
		print('\tChoose the correct option:')
	def right_option(self, rightOption):
		self.options = []
		self.options += [rightOption]
	def del_right_option(self, key, dict):
		self.wrongDict = dict.copy()
		del self.wrongDict[key]
	def add_wrong_translations(self, wrongDict):
		for word in wrongDict:
			self.options += [wrongDict[word]]
	def add_wrong_words(self, wrongDict):
		for word in wrongDict:
			self.options += [word]
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
	def output_words(self):
		self.options = self.options[0:self.numOptions]
		random.shuffle(self.options)
		i = 0
		for key in self.options:
			print(str(i + 1) + '.) ', key)
			i += 1
	def compare_option(self, 
					   choice, 
					   key):
		choice = [self.options[int(choice) - 1]]
		if ', ' in choice[0]:
			num = choice[0].find(', ')
			choice = choice[0][0:num]
		else:
			choice = choice[0]
		if choice in key:
			print('True ', choice)
		else:
			print('Wrong ', choice)
