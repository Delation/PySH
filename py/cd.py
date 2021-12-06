#!/bin/pysh
def cd(location:str = None):
	if location:
		path = args[0]
		os.chdir(path)
	return
