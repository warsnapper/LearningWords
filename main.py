
import shelve, random
from formDict import Output, InputValid, FormDict
from menu import Menu
from rememberWords import RememberWords
from choiceOption import ChoiceTranslations, ChoiceWords
from writeOption import WriteTranslate, WriteWord

db = shelve.open('testdb')

#############################################################################################

# CHOOSE WHAT WILL LEARN, EDITING OR ADD NEW 

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

#############################################################################################

customDict = dictOut.selectDict.copy() # in this dictionary, 
                                       # change the number of incorrect answers (position -1)
                                       # and the number of studies of this word (position -2)

def custom_dict(customDict, key): # called each time when was incorrect answer
	customDict[key][-1] += 1      # adds one to the total number of wrong answers

#############################################################################################

# FORMING THE DICTIONARY FOR THE STUDY

dictForm = FormDict()

dictForm.num_del(dictOut.selectDict, dictVal.choice)
while dictForm.numDel:
	dictForm.max_study(dictOut.selectDict)
	dictForm.min_wrongs(dictOut.selectDict)
	dictForm.reduction(dictOut.selectDict)
	dictForm.numDel -= 1

#############################################################################################

# REMEMBER THE WORDS

theseWords = RememberWords()

theseWords.remember_words(dictOut.selectDict, theseWords.forming)

#############################################################################################

# SELECT CORRECT OPTION

trans = ChoiceTranslations(dictOut.selectDict) 
transVal = InputValid()
words = ChoiceWords(dictOut.selectDict)
wordsVal = InputValid()

trans.num_options(dictVal.choice)

while trans.keysList or words.keysList:

	for key in trans.keysList:
		print('\n', key)
		print('\tSelect correct option:')
		trans.right_option(dictOut.selectDict[key])
		trans.del_right_option(key,
			                   dictOut.selectDict)
		trans.add_wrong_translations(trans.wrongDict)
		trans.output_translations(trans.translate_out)
		transVal.prompt()
		transVal.type_check(transVal.prompt)
		transVal.check_entry(1,
			                 trans.options,
			                 transVal.prompt,
			                 transVal.type_check)
		trans.compare_option(transVal.choice,
							 dictOut.selectDict[key],
							 key,
							 trans.translate_out,
							 trans.wrong_in_end,
							 custom_dict, customDict)
		break
	trans.del_right_answers()

	for key in words.keysList:
		supStr = words.translate_out(dictOut.selectDict[key][0:-2])
		print('\n', supStr)
		print('\tSelect correct option:')
		words.right_option(key)
		words.numOptions = trans.numOptions
		words.del_right_option(key,
			                   dictOut.selectDict)
		words.add_wrong_words(words.wrongDict)
		words.output_words()
		wordsVal.prompt()
		wordsVal.type_check(wordsVal.prompt)
		wordsVal.check_entry(1, words.options,
						     wordsVal.prompt,
						     wordsVal.type_check)
		words.compare_option(wordsVal.choice,
							 key, supStr,
							 words.wrong_in_end,
							 custom_dict, customDict)
		break
	words.del_right_answers()

#######################################################################

# WRITE OF THE TRANCLATION OF THE WORD OR THE WORD OF THE TRANCLATION 

writeTrans = WriteTranslate(dictOut.selectDict)
writeWord = WriteWord(dictOut.selectDict)

while writeTrans.keysList or writeWord.keysList:

	for key in writeTrans.keysList:
		print('\n', key)
		print('\tWrite the translation:')
		writeTrans.request()
		writeTrans.compare(key, 
						   dictOut.selectDict[key],
						   trans.translate_out,
						   writeTrans.wrong_in_end,
						   custom_dict,
						   customDict)
		break
	writeTrans.del_right_answers()

	for key in writeWord.keysList:
		supStr = words.translate_out(dictOut.selectDict[key][0:-2])
		print('\n', supStr)
		print('\tWrite the translation:')
		writeWord.request()
		writeWord.compare(key, 
						  supStr,
						  writeWord.wrong_in_end,
						  custom_dict,
						  customDict)
		break
	writeWord.del_right_answers()

#######################################################################

# to the number of studies adding 1
for key in dictOut.selectDict: # to the studied words
	customDict[key][-2] += 1   
db[db['listDict'][int(listVal.choice) - 1][0]] = customDict

#######################################################################

db.close()