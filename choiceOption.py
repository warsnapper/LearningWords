"""
def remember_words(studyDict):
	print('\n\tRemember the words:')
	for word in studyDict:
		singleStr = ''
		for translate in studyDict[word][0:-2]:
			singleStr += translate
			singleStr += ', '
		singleStr = singleStr[0:-2]
		print('\n', word, ' - ', singleStr)
		input()
"""

class RememberWords:
	"""docstring for RememberWords"""
	def forming(self):
		singleStr = ''
		for translate in studyDict[word][0:-2]:
			singleStr += translate + ', '
		singleStr = singleStr[0:-2]
		print('\n', word, ' - ', singleStr)
		input()
	def remember_words(self, forming):
		print('\n\tRemember the words:')
		global word
		for word in studyDict:
			forming()

class ChoiceVar:
	"""docstring for ChoiceVar"""
	def __init__(self):
		self.listForDel = []
	def num_options(self, studyDict):				
		if len(studyDict) >= 6:
			self.numOptions = 6
		else:
			self.numOptions = len(studyDict)
	def right_option(self, rightOption):
		self.options = []
		self.options += [rightOption[0:-2]]
	def del_right_option(self):
		self.singleDict = studyDict.copy()
		del self.singleDict[word]
	def add_wrong_options(self, wrongList):
		self.singleList = []
		for translat in wrongList:
			self.singleList += [translat[0:-2]]
		random.shuffle(self.singleList)
		self.singleList = self.singleList[0:self.numOptions-1]
		self.options += self.singleList
		random.shuffle(self.options)
	def output_options(self):
		self.supList = []
		for item in self.options: 
			self.singleStr = ''
			for it in item:
				self.singleStr += it + ', '
			self.singleStr = self.singleStr[0:-2]
			self.supList += [self.singleStr]
		i = 0
		for item in self.supList:
			print('\n' + str(i + 1) + '.) ', item)
			i += 1
	def correct_wrong(self, choice, it, customizDict, forming):
		if it in self.supList[int(choice) - 1]:
			self.listForDel += [word]
		else:
			print('Wrong')
			forming()
			customizDict[word][-1] += 1
	def del_correct_answers(self, theDict):
		for word in self.listForDel:
			del theDict[word]


if __name__ == '__main__':

	import shelve, random
	from choice import InputValid

	db = shelve.open('testdb')

	studyDict = db['python']

	theseWords = RememberWords()

	theseWords.remember_words(theseWords.forming)

	thisDict = ChoiceVar()
	thisCheck = InputValid()

	thisDict.num_options(studyDict)

	supDict = studyDict.copy()
	customizDict = db['python'].copy()

	while supDict:
		for word in supDict:
			print('\n\t', word, '\n',
				  '\n\tChoose the correct option:')
			thisDict.right_option(studyDict[word])
			thisDict.del_right_option()
			thisDict.add_wrong_options(thisDict.singleDict.values())
			thisDict.output_options()
			thisCheck.prompt()
			thisCheck.type_check(thisCheck.prompt)
			thisCheck.check_entry(-100, thisDict.supList, thisCheck.prompt, thisCheck.type_check)
			thisDict.correct_wrong(thisCheck.choice, studyDict[word][0], customizDict, theseWords.forming)
		thisDict.del_correct_answers(supDict)
		thisDict.listForDel = []
	
	db['python'] = customizDict
	print(db['python'])

	db.close()