#!/bin/pysh
def cat(filename:str):
	if not os.path.isfile(args[0]):
		raise FileNotFoundError('invalid file location')
	clear()
	lines, columns = Utility().get_size()
	with open(filename,'r') as file:
		rows = file.read().split('\n')
	print(f'{filename}'+'-'*(columns-len(filename)))
	for i in range(lines-3):
		try:print(rows[i][:columns])
		except:break
	if len(rows) > lines-3:
		print('-'*(columns-12)+'File cut off')
	else:
		print('-'*columns)
	return
