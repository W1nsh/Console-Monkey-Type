class TypingSession:
	len_str: int = 40 # Далее брать из виджета (расчитывать как-нибудь)
	len_current_str: int = 40 # Далее заменить на список длин строк, 1, 2, 3 + менять знач при добавлении текста

	def __init__(self, text: str, mode: str) -> None:
		self.text = text
		self.input_text = ''
		self.caret = 0 # Курсор ввода, равен позиции следующего символа для ввода
		self.char_position_statuses = {}
		self.mode = mode # time | words | sentences


	def generate_text(self, len_str: int) -> str:
		return "Заглушка"
	

	def parsing_new_sentence(self) -> str:
		return "Заглушка"

	
	def add_text(self, new_text: str) -> None:
		self.text += new_text
		# Добавлять только обрезанные по длине строки (хз где обрезать буду пока что)

	def add_char(self, char: str) -> None:
		self.input_text += char
		self.char_position_statuses[self.caret] = (char == self.text[self.caret])
		self.caret += 1
		if self.should_new_text():
			if self.mode == 'time' or self.mode == 'words':
				self.add_text(self.generate_text(self.len_str)) # Типа генерация текста, написать ф-цию в другом модуле. 
			elif self.mode == 'sentences':
				# Парсинг нового предложения
				self.add_text(self.parsing_new_sentence())


	def should_new_text(self) -> bool:
		if self.mode == 'time':
			# проверять время, дошел ли курсор ввода до середины ТЕКУЩЕЙ строки
			return True
		elif self.mode == 'words':
			# проверять кол-во введенных слов, проверять кол-во оставшихся слов,
			# если слов меньше чем надо, курсор на середине ТЕКУЩЕЙ строки - догенерировать
			return True
		elif self.mode == 'sentences':
			# проверять кол-во введенных предложений, кол-во оставшихся предложений,
			# если предложений меньше чем надо, курсор на середине ТЕКУЩЕЙ строки - спрасить новое предложение
			# и урезать по длине строки (макс), взятой от размеров виджета
			return True
		return False
		
