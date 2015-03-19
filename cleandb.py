
class CleanDB:
	"""
	Clears the database, 
	and then makes it the default values 
	for the test
	"""
	def __init__(self, db):
		self.db = db
	def cleaning(self):
		for key in self.db:
			del self.db[key]
	def recording(self):
		self.db['python'] = {'record': ['запись', 0, 0],
			                 'branch': ['филиал', 'отделение', 'ветвь', 0, 0],
			                 'field': ['поле', 'область', 0, 0],
			                 'trunk': ['ствол', 'туловище', 'багажник', 0, 0],
			                 'square': ['квадрат', 'площадь', 1, 2],
			                 'exception': ['исключение', 'непредвиденная ситуация', 1, 2],
			                 'row': ['строка', 'ряд', 1, 1],
			                 'input': ['вход', 'ввод', 1, 1],
			                 'statement': ['инструкция', 'декларация', 'изложение', 2, 2],
			                 'extension': ['расширение', 2, 2],
			                 'variable': ['переменная', 2, 3],
			                 'extend': ['продлить', 'распространить', 2, 1]} 
		self.db['fargo_s01e01_p1'] = {'tie': ['галстук', 0, 0]} 
		self.db['fargo_s01e01_p2'] = {'forearm': ['предплечье', 0, 0],
			                          'brain': ['мозг', 'интеллект', 0, 0]}      
		self.db['listDict'] = [['python', []], ['fargo_s01e01_p1', []], ['fargo_s01e01_p2', []]]
	def output(self):
		for key in self.db:
			print(key, '- ', self.db[key])

if __name__ == '__main__':
	import shelve
	db = shelve.open('testdb')
	dicts = CleanDB(db)
	dicts.cleaning() 
	dicts.recording()
	dicts.output()
	db.close()
