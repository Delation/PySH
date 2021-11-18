#!/bin/pysh
def cd(args:list = []):
	Utility().check_args(args,0,1)
	if args:
		path = args[0]
		os.chdir(path)
	return
