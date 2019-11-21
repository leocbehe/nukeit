import sys
import file_editor	

def get_params(fe):
	fe.params.filename = input("Please enter a filename, or press enter to quit.\n> ")
	if not fe.params.filename:
		return False
		
	fe.params.word = input("Please enter a word to nuke, or press enter to quit.\n> ")
	if not fe.params.word:
		return False
	
	tmp = input("Would you like to replace this word with another word? ( y/n ) or press enter to quit.\n> ")
	if not tmp:
		return False
	else:
		fe.params.replace = "y" in tmp.lower()
		
	if fe.params.replace:
		fe.params.replace_word = input("Please enter the replacement word, or press enter to quit.\n> ")
		if not fe.params.replace_word:
			return False
		
	return True

def loop_prompt(fe):
	continue_looping = True
	while continue_looping:
		if get_params(fe):
			fe.nuke()
		else:
			continue_looping = False

def main():
	pass
	fe = file_editor.FileEditor()
	if len(sys.argv) > 1:
		fe.params.filename = sys.argv[1]
		fe.nuke()
	else:
		loop_prompt(fe)
	print("Goodbye!")
		
if __name__ == "__main__":
	main()