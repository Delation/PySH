#! /PySH/cli
def cd(location:str = None):
	if location:
		os.chdir(location)
	return
