
import random
from choiceOption import ChoiceTranslations

class WriteTranslate(ChoiceTranslations):
	"""docstring for WriteTranslate"""
	def __init__(self, dict):
		self.forDel = []
		self.keysList = []
		for key in dict:
			self.keysList += [key]
		random.shuffle(self.keysList)
	def request(self):
		self.enter = input()
	def compare(self, key, value,
				translate_out, wrong_in_end,
				custom_dict, customDict):
		if self.enter in value:
			self.forDel += [key]
		else:
			supStr = translate_out(value[0:-2])
			print("\tIt's wrong!\n", key, ' - ', supStr)
			request = input('If you enter the correct variant type 1: ')
			if request == '1':
				value.insert(-2, self.enter)
				self.forDel += [key]
			else:
				wrong_in_end()
				custom_dict(customDict, key)

class WriteWord(WriteTranslate):
	"""docstring for WriteWord"""
	def __init__(self, dict):
		WriteTranslate.__init__(self, dict)
	def compare(self, key, supStr, wrong_in_end,
				custom_dict, customDict):
		if self.enter == key:
			self.forDel += [key]
		else:
			print("\tIt's wrong!\n", key, ' - ', supStr)
			input()
			wrong_in_end()
			custom_dict(customDict, key)