import params
import os

class FileEditor():
	
	def __init__(self):
		self.params = params.Params()
	
	def nuke(self):
		filename = self.params.filename
		if not self.valid_filename(filename):
			print("Filename \"" + filename + "\" is not valid!")
			return False
		temp_filename = self.write_new_file(filename)
		self.replace_old_file(temp_filename)
		
	def write_new_file(self, filename):
		temp_filename = self.get_temp_filename(filename)
		with open(temp_filename, "wt") as fout:
			with open(filename, "rt") as fin:
				for line in fin:
					nuke_string = self.params.word
					replacement = self.params.replace_word \
						if self.params.replace else ""
					new_line = line.replace(nuke_string, replacement)
					print(new_line, end='', file=fout)
		return temp_filename
	
	def valid_filename(self, filename):
		return os.path.isfile(filename)
		
	def replace_old_file(self, temp_filename):
		old_filename = temp_filename.replace("-new", "")
		os.remove(old_filename)
		os.rename(temp_filename, old_filename)
		print("File nuked.")
		# TODO: make safe for files that already include "-new" in filename
		
	def get_temp_filename(self, filename):
		ext_index = filename.rfind(".")
		filename_ext = filename[ext_index:]
		return filename[0:ext_index] + "-new" + filename_ext