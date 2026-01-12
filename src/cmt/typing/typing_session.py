from dataclasses import dataclass, field

from .char_status import CharStatus
from .char_state import CharState
from .mode_state import ModeState

@dataclass
class TypingSession:
	mode: ModeState
	text: str
	typed: list[str] = field(default_factory=list)
	char_statuses: dict[int, CharStatus] = field(default_factory=dict)
	caret: int = 0


	def append_text(self, new_text: str) -> None:
		"""Appends new text to the existing text."""
		self.text += new_text


	def forward_caret(self) -> None:
		"""Moves the caret one position forward."""
		self.caret += 1


	def backward_caret(self) -> None:
		"""Moves the caret one position backward."""
		self.caret -= 1

	
	def append_typed_char(self, char: str, state: CharState) -> None: # Принимается STATUS
		"""Appends a typed character and it's status."""
		self.typed.append(char) # А если 2 символа сразу?
		char_status = CharStatus(char=char, state=state)
		self.char_statuses[self.caret] = char_status # Почему не через caret?
		self.forward_caret() # Возможно надо будет убрать, если будет нужен другой порядок вызова в функциях (вероятно сторонних)


	def pop_typed_char(self):
		"""Removes the last typed character and it's status."""
		del self.char_statuses[self.caret - 1]
		self.typed.pop()
		self.backward_caret() # Возможно надо будет переписать порядок вызова.
		