def ls(*args):
	if len(args) > 0:
		print('# Notice of usage - unfinised command')
	lines, columns = Utility().get_size()
	o = os.listdir(os.getcwd())
	distance = ' '*int(columns/10)
	length = int(columns/len(max(o, key=len)))
	o = distance.join([ o[i] + (' '*(length - len(o[i]))) for i in range(len(o)) ])
	return '\n'.join([ o[i:i+columns].strip() for i in range(0, len(o), columns) ])
