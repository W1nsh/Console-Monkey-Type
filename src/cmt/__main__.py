from cmt.typing import TypingSession, TypingHandler, ModeState


session = TypingSession(ModeState.TIME, 'w1nsh')
handler = TypingHandler(session)

while len(session.typed) < len(session.text):
	caret = session.caret
	reference_char = session.text[caret]
	user_input = input(f'Input char \'{reference_char}\': ')
	if len(user_input) == 1:
		caret = session.caret
		reference_char = session.text[caret]
		handler.input_char(user_input)
		typed_char = session.typed[caret]
		char_state = session.char_statuses[caret].state
	elif user_input == 'backspace':
		caret = session.caret
		reference_char = session.text[caret]
		handler.backspace()
		typed_char = 'backspace'
		char_state = None
	else:
		typed_char = user_input
		char_state = None

	print(f'\nReference char: {reference_char}\nTyped char: {typed_char}\nChar state: {char_state}\nCaret: {session.caret}\n')
	
# This file now for tests only