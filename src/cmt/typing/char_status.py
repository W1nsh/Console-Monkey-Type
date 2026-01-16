from dataclasses import dataclass

from .char_state import CharState


@dataclass
class CharStatus:
	char: str
	state: CharState
