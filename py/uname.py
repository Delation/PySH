def uname(option:str = None):
	if not option:
		option = '-a'
	usage = Utility().require_opts([option,],['a','m','n','p','r','s','v'])
	if option == usage[0]:
		return ' '.join(os.uname())
	elif option == usage[1]:
		return platform.machine()
	elif option == usage[2]:
		return platform.node()
	elif option == usage[3]:
		return platform.processor()
	elif option == usage[4]:
		return platform.release()
	elif option == usage[5]:
		return platform.system()
	elif option == usage[6]:
		return platform.version()
