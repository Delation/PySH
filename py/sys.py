#!/bin/pysh
def sys(*args):
	if len(args) > 0:
		return os.system(' '.join(args))
	raise IndexError()
