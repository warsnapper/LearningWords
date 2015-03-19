
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
		i = 0
		for word in self.selectDict:
			print(str(i + 1) + '.) ', word, ' - ', self.selectDict[word])
			i += 1

class InputValid:
	"""
	Makes a request to a select element, 
	validates the input
	"""
	def prompt(self): # Must be entered as an integer
		self.choice = input('\nEnter the number: ')
	def type_check(self, request): # Put an integer?
		while True:
			try:
				self.test = int(self.choice)
				break
			except: 
				print('\nIncorrect input! Try again.')
				request()
	def check_entry(self, number, theList, request, type_check): # If the number you entered
		while True:
			if number <= int(self.choice) <= len(theList):
				break
			else:
				print('\nIncorrect input! Try again.')
				request()
				type_check(request) # you must ensure that choice is integer
				                    # otherwise "if", above, may cause an exception
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
	
if __name__ == '__main__':

	import shelve

	db = shelve.open('testdb')

	listOut = Output()

	listOut.list_output(db['listDict'])

	listVal = InputValid()

	listVal.prompt()
	listVal.type_check(listVal.prompt)
	listVal.check_entry(1, db['listDict'], listVal.prompt, listVal.type_check)

	dictOut = Output()

	dictOut.dict_output(listVal.choice, db)

	dictVal = InputValid()

	dictVal.prompt()
	dictVal.type_check(dictVal.prompt)
	dictVal.check_entry(1, dictOut.selectDict, dictVal.prompt, dictVal.type_check)

	dictForm = FormDict()

	dictForm.num_del(dictOut.selectDict, dictVal.choice)
	while dictForm.numDel:
		dictForm.max_study(dictOut.selectDict)
		dictForm.min_wrongs(dictOut.selectDict)
		dictForm.reduction(dictOut.selectDict)
		dictForm.numDel -= 1

	db.close()