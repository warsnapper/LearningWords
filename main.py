
import shelve, random
from formDict import *
from menu import Menu
from rememberWords import RememberWords
from choiceOption import ChoiceTranslations, ChoiceWords
from writeOption import WriteTranslate, WriteWord

db = shelve.open('testdb')

#############################################################################################

# CHOOSE WHAT WILL LEARN, EDITING OR ADD NEW 

listOut = Output()
insMenu = Menu()

def choice_dict(self_func):
	
	print('\n\tTo select, enter the number of the dictionary')
	insMenu.zero_print()
	listOut.list_output(db['listDict'])
	listOut.request(listOut.request, -10, db['listDict'])

	if int(listOut.choice) == 0: 
		insMenu.output_menu_list()
		listOut.request(listOut.request, -1, [])
		if int(listOut.choice) == -1:
			self_func(self_func)
		else:
			insMenu.name_newDict(db['listDict'])
			db['listDict'] = insMenu.theList
			db[insMenu.nameNewDict] = {}
			insMenu.add_newWord(db[insMenu.nameNewDict])
			db[insMenu.nameNewDict] = insMenu.newDict
			input()
			self_func(self_func)

choice_dict(choice_dict)

dictOut = Output()

def choice_words(self_func):

	print('\n\tEnter how many words to the study')
	insMenu.minus_one()
	insMenu.zero_print()
	dictOut.dict_output(listOut.choice, db)
	dictOut.request(dictOut.request, 
					-1, 
					dictOut.selectDict)

	if int(dictOut.choice) == 0:
		insMenu.output_menu_dict()
		dictOut.request(dictOut.request, -1, [])
		if int(dictOut.choice) == -1:
			self_func(self_func)
		elif int(dictOut.choice) == 0:
			insMenu.add_newWord(dictOut.selectDict)
			db[db['listDict'][int(listOut.choice) - 1][0]] = insMenu.newDict
			input()
			self_func(self_func)
	elif int(dictOut.choice) == -1:
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

dictForm.num_del(dictOut.selectDict, dictOut.choice)
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
transVal = Output()
words = ChoiceWords(dictOut.selectDict)
wordsVal = Output()

trans.num_options(dictOut.choice)

while trans.keysList or words.keysList:

	for key in trans.keysList:
		print('\n', key)
		print('\tSelect correct option:')
		trans.right_option(dictOut.selectDict[key])
		trans.del_right_option(key,
			                   dictOut.selectDict)
		trans.add_wrong_translations(trans.wrongDict)
		trans.output_translations(trans.translate_out)
		transVal.request(transVal.request,
						 1,
						 dictOut.selectDict)
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
		wordsVal.request(wordsVal.request,
					     1,
					     dictOut.selectDict)
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
						   customDict[key],
						   trans.translate_out,
						   writeTrans.wrong_in_end,
						   custom_dict,
						   customDict)
		break
	writeTrans.del_right_answers()

	for key in writeWord.keysList:
		supStr = words.translate_out(customDict[key][0:-2])
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
db[db['listDict'][int(listOut.choice) - 1][0]] = customDict

#######################################################################

db.close()