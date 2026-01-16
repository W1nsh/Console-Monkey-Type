from .typing.typing_session import TypingSession
from .typing.typing_handler import TypingHandler
from .typing.mode_state import ModeState


session = TypingSession(ModeState.TIME, 'w1nsh')
handler = TypingHandler(session)

while len(session.typed) < len(session.text):
	ui = str(input('Input char: '))
	char, state = handler.input_char(ui)
	print(f'Input: {ui}\nInput for Handler: {char}\nState char: {state}')
