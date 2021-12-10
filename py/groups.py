#! /PySH/cli
def groups(user = None):
	if not user:
		user = account.username
	for i in accounts:
		if i.username == user:
			return f'{i.username} ' + ' '.join(i.flags)
	raise ValueError('unknown account')
