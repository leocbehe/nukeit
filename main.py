import sys
import file_editor

def get_args():
	pass

def loop_prompt(file_editor):
	pass		

def main():
	pass
	fe = file_editor.FileEditor()
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		fe.nuke(filename)
	else:
		loop_prompt(fe)
	print("Goodbye!")
		
if __name__ == "__main__":
	main()