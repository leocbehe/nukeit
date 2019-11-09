class Params():
	
	def __init__(self):
		self.__continue_looping = True
		self.__word = ""
		self.__replace = False
		self.__replace_word = ""
		
	@property
	def continue_looping(self):
		return self.__continue_looping
		
	@continue_looping.setter
	def continue_looping(self, continue_looping):
		self.__continue_looping = continue_looping
		
	@property
	def word(self):
		return self.__word
		
	@word.setter
	def word(self, word):
		self.__word = word
		
	@property
	def replace(self):
		return self.__replace
		
	@replace.setter
	def replace(self, replace):
		self.__replace = replace
		
	@property
	def replace_word(self):
		return self.__replace_word
		
	@replace_word.setter
	def replace_word(self, replace_word):
		self.__replace_word = replace_word
