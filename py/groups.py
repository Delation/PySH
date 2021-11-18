#!/bin/pysh
def groups(args:list = []):
	Utility().check_args(args,0,1)
	args.append(account.username)
	for i in accounts:
		if i.username == args[0]:
			return f'{i.username} ' + ' '.join(i.flags)
	raise ValueError('unknown account')
