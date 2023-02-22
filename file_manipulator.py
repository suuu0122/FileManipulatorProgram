import sys

def validate_args():
	num_arguments = len(sys.argv)
	if (num_arguments < 4):
		print("Wrong arguments num!")
		sys.exit()
	use_method = sys.argv[1]
	if (use_method != "reverse" and use_method != "copy" and use_method != "duplicate-contents" and use_method != "replace-string"):
		print("Wrong method name!")
		sys.exit()
	if (use_method == "reverse"):
		if (num_arguments != 4):
			print("Wrong reverse method usage!")
			print("USAGE: python3 file_manipulator.py reverse input.txt output.txt")
			sys.exit()
	if (use_method == "copy"):
		if (num_arguments != 4):
			print("Wrong copy method usage!")
			print("USAGE: python3 file_manipulator.py copy input.txt output.txt")
			sys.exit()
	if (use_method == "duplicate-contents"):
		if (num_arguments != 5):
			print("Wrong duplicate-contents method usage!")
			print("USAGE: python3 file_manipulator.py duplicate-contents input.txt output.txt num_dup")
			sys.exit()
	if (use_method == "replace-string"):
		if (num_arguments != 6):
			print("Wrong replace-string method usage!")
			print("USAGE: python3 file_manipulator.py replace-string input.txt output.txt needle new_string")
			sys.exit()

def reverse(contents):
	return contents[::-1]

def copy(contents):
	return contents

def duplicate_contents(contents, num_dup):
	return contents * num_dup

def replace_string(contents, needle, new_string):
	return contents.replace(needle, new_string)

def main():
	validate_args()
	use_method = sys.argv[1]
	input_file_path = sys.argv[2]
	output_file_path = sys.argv[3]
	with open(input_file_path) as input_f:
		contents = input_f.read()
		if (use_method == "reverse"):
			new_contens = reverse(contents)
		elif (use_method == "copy"):
			new_contens = copy(contents)
		elif (use_method == "duplicate-contents"):
			num_dup = int(sys.argv[4])
			new_contens = duplicate_contents(contents, num_dup)
		elif (use_method == "replace-string"):
			needle = sys.argv[4]
			new_string = sys.argv[5]
			new_contens = replace_string(contents, needle, new_string)
	with open(output_file_path, 'w') as output_f:
		output_f.write(new_contens)

if __name__ == "__main__": 
    main()
