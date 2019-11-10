import sys
import file_editor

def get_params(fe):
	# prompt for each value
	# if any value returned is empty, return false
	return False

def loop_prompt(fe):
	continue_looping = True
	while continue_looping:
		continue_looping = get_params(fe)
		fe.nuke()

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