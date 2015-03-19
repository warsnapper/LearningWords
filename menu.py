
class Menu:
	"""docstring for Menu"""
	def zero_print(self):
		print(' 0.) menu')
		print(' -' * 14)
	def minus_one(self):
		print('-1.) back')

if __name__ == '__main__':

	insMenu = Menu()

	insMenu.minus_one()
	insMenu.zero_print()
		