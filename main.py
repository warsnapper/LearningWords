
import shelve, random
from formDict import Output, InputValid, FormDict
from menu import Menu
from rememberWords import RememberWords
from test2 import ChoiceTranslations, ChoiceWords

db = shelve.open('testdb')

listOut = Output()
insMenu = Menu()
listVal = InputValid()

def choice_dict(self_func):
	
	print('\n\tTo select, enter the number of the dictionary')
	insMenu.zero_print()
	listOut.list_output(db['listDict'])

	listVal.prompt() # Query for the number of dictionary
	listVal.type_check(listVal.prompt) # Integer if the number entered?
	listVal.check_entry(0, db['listDict'], listVal.prompt, listVal.type_check) # In need whether it is the range?

	if int(listVal.choice) == 0: 
		print('Sorry! This functionality is not yet available.\n')
		input()
		self_func(self_func)

choice_dict(choice_dict)

dictOut = Output()
dictVal = InputValid()

def choice_words(self_func):

	print('\n\tEnter how many words to the study')
	insMenu.minus_one()
	insMenu.zero_print()
	dictOut.dict_output(listVal.choice, db)

	dictVal.prompt()
	dictVal.type_check(dictVal.prompt)
	dictVal.check_entry(-1, dictOut.selectDict, dictVal.prompt, dictVal.type_check)

	if int(dictVal.choice) == 0:
		print('Sorry! This functionality is not yet available.\n')
		input()
		self_func(self_func)
	elif int(dictVal.choice) == -1:
		choice_dict(choice_dict)
		self_func(self_func)

choice_words(choice_words)

dictForm = FormDict()

dictForm.num_del(dictOut.selectDict, dictVal.choice)
while dictForm.numDel:
	dictForm.max_study(dictOut.selectDict)
	dictForm.min_wrongs(dictOut.selectDict)
	dictForm.reduction(dictOut.selectDict)
	dictForm.numDel -= 1

theseWords = RememberWords()

theseWords.remember_words(dictOut.selectDict, theseWords.forming)

trans = ChoiceTranslations(dictOut.selectDict) # choose the correct translation
transValid = InputValid()
words = ChoiceWords(dictOut.selectDict)
wordsValid = InputValid()

for key in dictOut.selectDict:
	
	trans.num_options(dictVal.choice) 
	trans.out_word(key)
	trans.right_option(trans.dictionary[key])
	trans.del_right_option(key, trans.dictionary)
	trans.add_wrong_translations(trans.wrongDict)
	trans.output_translations(trans.translate_out)
	transValid.prompt()
	transValid.type_check(transValid.prompt)
	transValid.check_entry(1, trans.options, transValid.prompt, transValid.type_check)
	trans.compare_option(transValid.choice, trans.dictionary[key])
		
	words.numOptions = trans.numOptions
	supStr = words.translate_out(words.dictionary[key][0:-2])
	print(supStr)
	words.out_word(supStr)
	words.right_option(key)
	words.del_right_option(key, words.dictionary)
	words.add_wrong_words(words.wrongDict)
	words.output_words()
	wordsValid.prompt()
	wordsValid.type_check(wordsValid.prompt)
	wordsValid.check_entry(1, words.options, wordsValid.prompt, wordsValid.type_check)
	words.compare_option(wordsValid.choice, key)
	
db.close()