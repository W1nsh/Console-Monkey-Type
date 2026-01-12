from .typing_session import TypingSession


class TypingHandler:
	def __init__(self, session: TypingSession) -> None:
		self.session = session

	
	def input_char(self, char: str) -> None:
		pass # Заглушка


	def backspace(self) -> None:
		pass # Заглушка


	def ctrl_backspace(self) -> None:
		pass # Заглушка
