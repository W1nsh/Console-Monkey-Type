from .typing_session import TypingSession
from .char_state import CharState


class TypingHandler:
	def __init__(self, session: TypingSession) -> None:
		self.session = session

	
	def input_char(self, char: str) -> None:
		if len(char) == 1:
			char_state = self.get_char_state(char, self.session.caret)
			self.session.append_typed_char(char, char_state)
			if (char == ' ' and 
	   			char_state in (CharState.CORRECT, CharState.CORRECTED)):
				self.space()


	def space(self) -> None:
		pass


	def backspace(self) -> None:
		if self.session.caret > 0:
			self.session.pop_typed_char()


	def ctrl_backspace(self) -> None:
		pass 


	def get_mode_class_name(self) -> str:
		mode_name = self.session.mode.value.capitalize()
		return f'{mode_name}Mode'


	def get_char_state(self, char: str, position: int) -> CharState:
		if char == self.session.text[position]:
			last_char = self.session.char_statuses.get(position, None)
			if last_char:
				if last_char.state in (CharState.INCORRECT, CharState.CORRECTED):
					return CharState.CORRECTED
			return CharState.CORRECT
		return CharState.INCORRECT
