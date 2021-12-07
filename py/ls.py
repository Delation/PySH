#!/bin/pysh
def ls(*args):
	print('# Notice of usage - unfinised command')
	# Currently, since I'm a couch potato, this command simply just redirects into
	# the system's implementation of it
	# No regard for whether or not the command actually exists, might I add.
	return os.system(f'ls {" ".join(args)}')
	# In-work implementation
	lines, columns = Utility().get_size()
	o = ' '.join(os.listdir(os.getcwd()))
	return '\n'.join(o[i:i+columns] for i in range(0, len(o), columns))
