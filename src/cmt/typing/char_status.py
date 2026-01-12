from dataclasses import dataclass

from .char_state import CharState


@dataclass
class CharStatus:
	char: str
	state: CharState
	# count of all errors
	# count of all changes
