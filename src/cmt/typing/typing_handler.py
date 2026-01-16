from .typing_session import TypingSession
from .char_state import CharState


class TypingHandler:
	def __init__(self, session: TypingSession) -> None:
		self.session = session

	
	def input_char(self, char: str) -> tuple[str, CharState]:
		if len(char) == 1:
			char_state = self.get_char_state_2(char, self.session.caret)
			self.session.append_typed_char(char, char_state)
			return(char, char_state)
		return('netu nihuya', CharState.INCORRECT)

	def backspace(self) -> None:
		pass # Заглушка


	def ctrl_backspace(self) -> None:
		pass # Заглушка


	def get_mode_class_name(self) -> str:
		mode_name = self.session.mode.value.capitalize()
		return f'{mode_name}Mode'


	def get_char_state(self, char: str, position: int) -> CharState:
		if char == self.session.text[position]:
			state = CharState.CORRECT
		else:
			state = CharState.INCORRECT
		last_char = self.session.char_statuses.get(position, None)
		if last_char:
			if (state == CharState.CORRECT and
	   			last_char.state in (CharState.INCORRECT, CharState.CORRECTED)):
				state = CharState.CORRECTED
		return state

# Choose between this func (2) and func (1, up)
	def get_char_state_2(self, char: str, position: int) -> CharState:
		if char == self.session.text[position]:
			last_char = self.session.char_statuses.get(position, None)
			if last_char:
				if last_char.state in (CharState.INCORRECT, CharState.CORRECTED):
					return CharState.CORRECTED
			return CharState.CORRECT
		return CharState.INCORRECT
