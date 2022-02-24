def python():
	# A lacking Python interpreter
	# Users do not have root Python access
	while True:
		cmd = input('>>> ')
		if cmd.startswith('exit'):
			break
		elif cmd.startswith('help'):
			print('Available variables:')
			func = globals().copy()
			del func['__builtins__']
			print('\n'.join(func))
		else:
			try:
				exec(cmd)
			except Exception as e:
				print(f'{shell}: {inspect.stack()[0][3]}: {e}')
	return
