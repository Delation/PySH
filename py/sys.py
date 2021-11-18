#!/bin/pysh
def sys(args:list = []):
	Utility().check_args(args,1,999)
	return os.system(' '.join(args))
