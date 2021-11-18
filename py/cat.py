#!/bin/pysh
def cat(args:list = []):
	Utility().check_args(args,1,1)
	if not os.path.isfile(args[0]):
		raise FileNotFoundError('invalid file location')
	clear()
	lines, columns = Utility().get_size()
	with open(args[0],'r') as file:
		rows = file.read().split('\n')
	print(f'{args[0]}'+'-'*(columns-len(args[0])))
	for i in range(lines-3):
		try:print(rows[i][:columns])
		except:break
	if len(rows) > lines-3:
		print('-'*(columns-12)+'File cut off')
	else:
		print('-'*columns)
	return
