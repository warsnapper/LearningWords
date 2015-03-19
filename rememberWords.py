
class RememberWords:
	"""
	Displays in a convenient form of words to remember. 
	Divided into two methods, 
	in order to use the method of "forming" 
	for the formation of the output 
	of one word when you select the wrong option.
	"""
	def forming(self, studyDict):
		singleStr = ''
		for translate in studyDict[self.word][0:-2]:
			singleStr += translate + ', '
		singleStr = singleStr[0:-2]
		print('\n', self.word, ' - ', singleStr)
		input()
	def remember_words(self, studyDict, forming):
		print('\n\tRemember the words:')
		for self.word in studyDict:
			forming(studyDict)

if __name__ == '__main__':

	import shelve

	db = shelve.open('testdb')

	studyDict = db['python']

	theseWords = RememberWords()

	theseWords.remember_words(studyDict, theseWords.forming)

	db.close()