def help():
	func = globals().copy()
	del func['__builtins__']
	del func['utility']
	commands = []
	func = [ commands.append(i) for i in func if callable(func[i]) ]
	return 'Available functions:\n'+' '.join(commands)
