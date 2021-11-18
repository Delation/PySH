#!/bin/pysh
def clear(args:list = []):
	Utility().check_args(args)
	print('\033[H\033[J', end='')
	return
