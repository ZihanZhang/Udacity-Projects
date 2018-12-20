import os


def renamefiles():
	filenames = os.listdir("/Users/ZihanZhang/Documents/Projects/Udacity/prank")
	print(filenames)
	# curlo = os.getcwd()
	# print(curlo)
	os.chdir("/Users/ZihanZhang/Documents/Projects/Udacity/prank")
	for filename in filenames:
		os.rename(filename, filename.translate(None, "0123456789"))
	filenames = os.listdir("/Users/ZihanZhang/Documents/Projects/Udacity/prank")
	print(filenames)        # this filenames is the same as the upper one if not adding the upper code
	os.chdir("/Users/ZihanZhang/Documents/Projects/Udacity")


renamefiles()
