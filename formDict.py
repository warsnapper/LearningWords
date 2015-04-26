
class Output:
	"""
	Conclusion content,
	proposal to the selection
	"""
	def list_output(self, theList): # Displays the list of testdb
		self.theList = theList
		i = 0
		for elem in self.theList:
			print(str(i + 1) + '.) ', elem[0])
			i += 1
	def dict_output(self, choice, db): # Displays the contents of a dictionary
		self.choice = choice
		self.selectDict = db[db['listDict'][int(self.choice) - 1][0]]
		self.listWords = []
		for word in self.selectDict:
			self.listWords += [word]
		i = 0
		for word in self.listWords:
			print(str(i + 1) + '.) ', word, ' - ', self.selectDict[word])
			i += 1
	def request(self, self_func, number, theList):
		self.choice = input('\nEnter the number: ')
		try:
			test = int(self.choice)
		except:
			print('\nIncorrect input! Try again.')
			self_func(self_func, number, theList)
		else:
			if number <= int(self.choice) <= len(theList):
				pass
			else:
				print('\nIncorrect input! Try again.')
				self_func(self_func, number, theList)

class FormDict:
	"""
	Forming study dictionary.
	"""
	def num_del(self, dict, choice):
		self.numDel = len(dict) - int(choice)
	def max_study(self, dict):
		supList = []
		for key in dict:
			supList += [dict[key][-2]]
		self.maxStudy = max(supList)
	def min_wrongs(self, dict):
		supList = []
		for key in dict:
			if dict[key][-2] == self.maxStudy:
				supList += [dict[key][-1]]
		self.minWrongs = min(supList)
	def reduction(self, dict):
		for key in dict:
			if dict[key][-2] == self.maxStudy and dict[key][-1] == self.minWrongs:
				del dict[key]
				break
	
